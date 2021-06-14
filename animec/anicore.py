# -*- coding: utf-8 -*-

import re

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError

class Anime:
    """Retrieves anime info via `animesonglyrics <https://www.animesonglyrics.com/>`__.

    Parameters
    ----------
    query: `str <https://docs.python.org/3/library/string.html#module-string>`__
        The query to be searched for.

    Attributes
    ----------
    url
        Returns the url of the anime main page
    name 
        Returns the main name of the anime
    
    title_english
        Returns the english title
    title_jp
        Returns the japanese title
    alt_titles
        Returns alternative titles
    
    episodes
        The episode count of the anime
    aired
        Anime's airing time
    broadcast
        The broadcast day of the series
    rating
        Rating given to the anime
    ranked
        Anime's ranking
    popularity
        The popularity of the anime
    favorites
        Count of people who tagged the anime as their favourite

    type
        Series type
    status
        Series current status with reference to airing
    producers: `list <https://docs.python.org/3/tutorial/datastructures.html>`__
        List of studios which contributed to the production of the series
    genres: `list <https://docs.python.org/3/tutorial/datastructures.html>`__
        List of anime genres or kind
    
    description
        Short description about the anime
    poster
        Anime thumbnail
    teaser
        Anime teaser/promotion either official or unofficial
    opening_themes: `list <https://docs.python.org/3/tutorial/datastructures.html>`__
        Opening themes of the series
    ending_themes: `list <https://docs.python.org/3/tutorial/datastructures.html>`__
        Ending themes of the series
    """

    def __init__(self, query: str):

        if " " in query:
            query = query.replace(" ", "%20")

        to_open = f"https://myanimelist.net/anime.php?q={query}"

        encoded_url = to_open.encode('ascii','ignore')
        try:
            html_page = urlopen(encoded_url.decode('utf-8'))
        except HTTPError:
            raise NotFound("Can't find a matching result." + f" Code: {HTTPError.code}")
        
        soup = BeautifulSoup(html_page, 'html.parser')

        anime_div = soup.find("td", {'class': 'borderClass bgColor0'})
        url = anime_div.find("a", href = True)['href']

        anime_page_open = urlopen(url)
        anime_page = BeautifulSoup(anime_page_open, 'html.parser')
        
        name = anime_page.find("h1", {'class' : 'title-name h1_bold_none'})

        spaceit_divs = anime_page.findAll('div', {'class' : 'spaceit_pad'})
        spaced_divs = anime_page.findAll('div', {'class' : 'spaceit'})
        dark_text = anime_page.findAll('span', {'class':'dark_text'})
        
        title_english = self._divCh_(div = spaceit_divs, txt = "English:")
        title_jp = self._divCh_(div = spaceit_divs, txt = "Japanese:")
        alt_titles = self._divCh_(div = spaceit_divs, txt = "Synonyms:")

        episodes = self._divCh_(div = spaced_divs, txt = "Episodes:")
        aired = self._divCh_(div = spaced_divs, txt = "Aired:")
        broadcast = self._divCh_(div = spaced_divs, txt = "Broadcast:")
        
        rating = self._parent_(element = dark_text, txt = "Rating:")
        popularity = self._parent_(element = dark_text, txt = "Popularity:")
        favorites = self._parent_(element = dark_text, txt = "Favorites:")
        _type = self._parent_(element = dark_text, txt = "Type:")
        status = self._parent_(element = dark_text, txt = "Status:")
        producers = self._parent_(element = dark_text, txt = "Producers:").split(", ")
        genres = self._parent_(element = dark_text, txt = "Genres:").split(", ")

        ranked_text = str(anime_page.find('div', {'class':'spaceit po-r js-statistics-info di-ib'}))
        ranked = re.search("#.*<", ranked_text)
        ranked = ranked.group().split("<")[0] if ranked else None

        description = anime_page.find('p', {'itemprop' : 'description'}).text
        poster = anime_page.find('img', {'itemprop' : 'image'})['data-src']

        opening_themes = [theme.text for theme in anime_page.find('div', {'class':'theme-songs js-theme-songs opnening'}).findChildren('span', {'class':'theme-song'})]
        ending_themes = [theme.text for theme in anime_page.find('div', {'class':'theme-songs js-theme-songs ending'}).findChildren('span', {'class':'theme-song'})]

        self.url = url or None
        self.name = name.text or None
        
        self.title_english = title_english or None
        self.title_jp = title_jp or None
        self.alt_titles = alt_titles or None

        self.episodes = episodes or None
        self.aired = aired or None
        self.broadcast = broadcast or None
        self.rating = rating or None
        self.ranked = ranked or None
        self.popularity = popularity or None
        self.favorites = favorites or None

        self.type = _type or None
        self.status = status or None
        self.producers = producers
        self.genres = genres or None

        self.description = description or None
        self.poster = poster or None
        self.opening_themes = opening_themes or None
        self.ending_themes = ending_themes or None

    def is_nsfw(self) -> bool:
        """
        Returns
        -------
        bool
            Returns if the series is nsfw
        """

        return "Nudity" in self.rating

    @property
    def teaser(self):

        url = urlopen(self.url + "/video")
        soup = BeautifulSoup(url, 'html.parser')

        div = soup.find('div', {'class' : 'video-list-outer po-r pv'})
        teaser_link = div.findChildren('a', {'class' : "iframe js-fancybox-video video-list di-ib po-r"})[0]['href']

        if teaser_link and "youtube" in teaser_link:
            _id = teaser_link.split("embed/")[1].split("?")[0]
            teaser_link = f"https://www.youtube.com/watch?v={_id}"

        return teaser_link or None

    def _divCh_(self, div: list, txt: str):

        for container in div:
            if txt in container.text:
                div_text = container.text.split(txt)[1].split()
                return " ".join(div_text)

    def _parent_(self, element: list, txt: str):

        for e in element:
            if txt in e.text:
                returned_text = e.parent.text.split(txt)[1].split()
                return " ".join(returned_text)

    def recommend(self) -> list:
        """
        Returns
        -------
        list
            Returns suitable recommendations based on the anime referred while declaring the class
        """
        
        anime_page = urlopen(f"{self.url}/userrecs")
        soup = BeautifulSoup(anime_page, 'html.parser')

        headers = soup.findAll("strong", limit = 15)

        recommendations = [i.get_text() for i in headers]

        ri = [i for i in recommendations if not i.isdigit()]  
        ri.pop(0)

        return ri[:5]

class NotFound(Exception):
    """Raised when no result is found or a HTTP error is raised"""
    
    pass
