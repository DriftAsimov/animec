import animec.gs
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

class charsearch:
    
    def __init__(self, query):

        url = find_character(query)

        if url is None:
            raise NoCharacterFound
            return

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

class NoCharacterFound(Exception):
    pass

def find_character(query):

    for url in animec.gs.search(f"{query} anime character info", num_results = 50):
        if ('myanimelist' in str(url)) and ('character' in str(url)):
            return url
