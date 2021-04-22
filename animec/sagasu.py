import animec.gs
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

class NoResultFound(Exception):
    pass

class charsearch:
    
    def __init__(self, query):

        url = _searchChar_(query = query)

        if url is None:
            raise NoResultFound("No such anime character found.")

        html_page = urlopen(url)
        soup = BeautifulSoup(html_page, 'html.parser')

        images = soup.findAll('img')

        string_list = [str(i) for i in images]

        for k in string_list:
            if 'characters' in k:
                char = k
                break

        image_url = re.search("https://.*jpg", char).group()

        title = soup.find('h2')
        title = title.get_text()

        self.title = title
        self.url = url
        self.image_url = image_url

def _searchChar_(query):
    
    for url in animec.gs.search(f"site:myanimelist.net {query} anime character info", num_results = 50):
        if ('myanimelist' in str(url)) and ('character' in str(url)):
            return url

def _searchLyrics_(query):

    for url in animec.gs.search(f"site:animesonglyrics.com {query}", num_results = 5):
        if 'animesonglyrics' in str(url):
            return url

def _lyricsType_(soup, div):

    lyrics_container = soup.find("div", {'id' : div}).text
    filtered_page = lyrics_container.split("Correct")[0]

    lyrics = filtered_page[:-50]
    lyrics = str(re.sub(' +', ' ', lyrics))

    return lyrics

class anilyrics:

    def __init__(self, query):

        url = _searchLyrics_(query)

        if url is None:
            raise NoResultFound("No lyrics for this song found.")

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
        req = Request(url = url, headers = headers)

        lyrics_page = urlopen(req).read()
        soup = BeautifulSoup(lyrics_page, 'html.parser')

        for breaks in soup.findAll("br"):
            breaks.replace_with("\n")

        romaji_lyrics = _lyricsType_(soup = soup, div = 'tab1')
        english_lyrics = _lyricsType_(soup = soup, div = 'tab2')
        kanji_lyrics = _lyricsType_(soup = soup, div = 'tab3')

        self.url = _searchLyrics_(query)
        
        self.romaji = romaji_lyrics
        self.english = english_lyrics
        self.kanji = kanji_lyrics
