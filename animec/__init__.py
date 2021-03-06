#IMPORTS

from googlesearch import search
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

'''
This is an unofficial module to extract an anime character data from ://myanimelist.net/
'''

__author__ = "DriftAsimov"
__title__ = "animec"
__copyright__ = "Copyright Drift Asimov 2021"
__version__ = "0.0.3"
__license__ = "MIT"

#IMPLEMENTATION
class Character:
    
    def __init__(self, query):
        self.query = query

    def search(self):
        
        try:
            
            result = {}

            for j in search(f"{self.query} anime character", tld="com", num=50, stop=50, pause=3):
                if 'myanimelist' in j:
                    url = j

            result["url"] = url

            html_page = urlopen(url)
            soup = BeautifulSoup(html_page, 'html.parser')

            images = soup.findAll('img')

            string_list = []

            for i in images:
                string_list.append(str(i))

            for k in string_list:
                if 'characters' in k:
                    char = k

            image_url = char.split('data-src="')[1][:-3]
            
            result["image"] = image_url

            title = soup.find('h2')
            title = title.get_text()

            result["title"] = title

            return result
        
        except Exception as e:
            print(e)
