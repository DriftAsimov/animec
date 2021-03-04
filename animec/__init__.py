#IMPORTS

from googlesearch import search
from bs4 import BeautifulSoup
from urllib.request import urlopen

#IMPLEMENTATION
class Animec:
    
    def animechar(self, query):
        
        try:
            
            for j in search(query, tld="com", num=50, stop=50, pause=3):
                if 'myanimelist' in j:
                    url = j

            html_page = urlopen(url)
            soup = BeautifulSoup(html_page, 'html.parser')

            images = soup.findAll('img')

            string_list = []

            for i in images:
                string_list.append(str(i))

            for i in string_list:
                if 'characters' in i:
                    char = i

            image_url = char.split('data-src="')[1][:-3]
            
            return image_url
        
        except Exception as e:
            print(e)

    def charinfo(self, query):

        try:

            for j in search(query, tld="com", num=50, stop=50, pause=3):
                if 'myanimelist' in j:
                    char_info = j
            
            return char_info

        except Exception as e:
            print(e)