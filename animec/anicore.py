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
    
    description
        Short description about the anime
    poster
        Anime thumbnail
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
            raise NotFound404("Can't find a matching result.")
        
        soup = BeautifulSoup(html_page, 'html.parser')

        anime_div = soup.find("td", {'class': 'borderClass bgColor0'})
        url = anime_div.find("a", href = True)

        anime_page_open = urlopen(url['href'])
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

        ranked_text = str(anime_page.find('div', {'class':'spaceit po-r js-statistics-info di-ib'}))
        ranked = re.search("#.*<", ranked_text)
        ranked = ranked.group().split("<")[0] if ranked else None

        description = anime_page.find('p', {'itemprop' : 'description'}).text
        poster = anime_page.find('img', {'itemprop' : 'image'})

        opening_themes = [theme.text for theme in anime_page.find('div', {'class':'theme-songs js-theme-songs opnening'}).findChildren('span', {'class':'theme-song'})]
        ending_themes = [theme.text for theme in anime_page.find('div', {'class':'theme-songs js-theme-songs ending'}).findChildren('span', {'class':'theme-song'})]

        self.url = url['href']
        self.name = name.text
        
        self.title_english = title_english
        self.title_jp = title_jp
        self.alt_titles = alt_titles

        self.episodes = episodes
        self.aired = aired
        self.broadcast = broadcast
        self.rating = rating
        self.ranked = ranked
        self.popularity = popularity
        self.favorites = favorites

        self.description = description
        self.poster = poster['data-src']
        self.opening_themes = opening_themes
        self.ending_themes = ending_themes

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

    def recommend(self):
        """
        Returns suitable recommendations based on the anime referred while declaring the class. 
        
        Returns
        -------
        list
            The list containing the recommendations
        """
        
        anime_page = urlopen(f"{self.url}/userrecs")
        soup = BeautifulSoup(anime_page, 'html.parser')

        headers = soup.findAll("strong", limit = 15)

        recommendations = [i.get_text() for i in headers]

        ri = [i for i in recommendations if not i.isdigit()]  
        ri.pop(0)

        return ri[:4]

class NotFound404(Exception):
    """Raised when No Result is Found"""
    
    pass
