#IMPORTS

from googlesearch import search
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

'''
This is an unofficial module to extract an anime character data from https://myanimelist.net/
'''

__author__ = "DriftAsimov"
__title__ = "animec"
__copyright__ = "Copyright Drift Asimov 2021"
__version__ = "0.0.5"
__license__ = "MIT"

#IMPLEMENTATION
class charsearch:
    
    def __init__(self, query):

        for j in search(f"{query} anime character", tld="com", num=50, stop=50, pause=3):
            if ('myanimelist') in j:
                url = j
                break

        try:
            
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
        
        except:
            print("No such anime character found.")
