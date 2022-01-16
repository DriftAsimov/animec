# -*- coding: utf-8 -*-

import re
import random

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from urllib.parse import quote

from .helpers import search
from .errors import NoResultFound


class Charsearch:
    """
    Retrieves anime character info via `MyAnimeList <https://myanimelist.net/>`__.

    Parameters
    ----------
    query: `str <https://docs.python.org/3/library/string.html#module-string>`__
        The query to be searched for.

    Attributes
    ----------
    url
        The url to access the character info page.
    title
        The name of the character found.
    image_url
        The url of the image of the character found.
    references: `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`__
        The series the character is referred in.
    """

    def __init__(self, query: str):

        url = _searchChar_(query=query)

        if url is None:
            raise NoResultFound("No such anime character found.")

        safe_url = quote(url, safe=' <>="/:!')

        html_page = urlopen(safe_url)
        soup = BeautifulSoup(html_page, "html.parser")

        images = soup.findAll("img")

        string_list = [str(i) for i in images]

        for k in string_list:
            if "characters" in k:
                char = k
                break

        image_url = re.search("https://.*jpg", char).group()

        title = soup.find("h2")
        title = title.get_text()

        references_base = soup.findAll(
            "td", {"valign": "top", "class": "borderClass"}, limit=10
        )
        references_raw = [
            i.findChildren("a", recursive=False)
            for i in references_base
            if i.findChildren("a", recursive=False)
        ]

        references = {}

        for reference in references_raw:

            reference_title = reference[0].text
            reference_url = reference[0]["href"]

            references[reference_title] = reference_url

        self.title = title
        self.url = url
        self.image_url = image_url
        self.references = references


def _searchChar_(query):

    for url in search(f"site:myanimelist.net/character {query}", num_results=50):
        if ("myanimelist" in str(url)) and ("character" in str(url)):
            return url


def _searchLyrics_(query):

    for url in search(f"site:animesonglyrics.com {query}", num_results=5):
        if "animesonglyrics" in str(url):
            return url


class Anilyrics:
    """
    Retrieves anime lyrics via `animesonglyrics <https://www.animesonglyrics.com/>`__.

    Parameters
    ----------
    query: `str <https://docs.python.org/3/library/string.html#module-string>`__
        The query to be searched for.

    Attributes
    ----------
    url
        The url to access the lyrics page.
    """

    def __init__(self, query):

        url = _searchLyrics_(query)

        if not url:
            raise NoResultFound("No lyrics for this song found.")

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"
        }
        req = Request(url=url, headers=headers)

        lyrics_page = urlopen(req).read()
        soup = BeautifulSoup(lyrics_page, "html.parser")

        for breaks in soup.findAll("br"):
            breaks.replace_with("\n")

        self.url = _searchLyrics_(query)
        self._soup = soup

    def _lyricsType_(self, div):

        lyrics_container = self._soup.find("div", {"id": div}).text
        filtered_page = lyrics_container.split("Correct")[0]

        lyrics = filtered_page[:-50]
        lyrics = str(re.sub(" +", " ", lyrics)).strip()

        return lyrics

    def romaji(self) -> str:
        """
        Returns
        -------
        list
            Lyrics in their romaji translation
        """

        romaji_lyrics = self._lyricsType_("tab1")
        return romaji_lyrics

    def english(self) -> str:
        """
        Returns
        -------
        str
            Lyrics in their english translation
        """

        english_lyrics = self._lyricsType_("tab2")
        return english_lyrics

    def kanji(self) -> str:
        """
        Returns
        -------
        str
            Lyrics in their kanji translation
        """

        kanji_lyrics = self._lyricsType_("tab3")
        return kanji_lyrics

    romanji = romaji


def kao(count: int = 1) -> list:
    """
    Parameters
    ----------
    count: `int`
        Number of kaomojis to request

    Returns
    -------
    list
        List comprising of random kaomojis
    """

    URL = "http://kaomoji.ru/en/"

    html_page = urlopen(URL)
    soup = BeautifulSoup(html_page, "html.parser")

    tables = soup.findAll("table", {"class": "table_kaomoji"})

    kaomojis = []

    for table in tables:

        kaomoji = table.findChildren("td")

        for i in kaomoji:

            kaomojis.append(str(i.text))

    kao = random.sample(kaomojis, count)

    return kao
