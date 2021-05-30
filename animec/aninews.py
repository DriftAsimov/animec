from bs4 import BeautifulSoup
from urllib.request import urlopen

class TooManyRequests(Exception):
    pass

class Aninews:
    """Retrieves Anime News via `MyAnimeList <https://myanimelist.net/>`__.

    Parameters
    ----------
    amount: `int <https://docs.python.org/3/library/functions.html#int>`__
        The amount of news articles to be fetched. Defaults to ``3``

    Attributes
    ----------
    titles: `list <https://docs.python.org/3/tutorial/datastructures.html>`__
        The retrieved news titles.
    links: `list <https://docs.python.org/3/tutorial/datastructures.html>`__
        The retrieved news links.
    description: `list <https://docs.python.org/3/tutorial/datastructures.html>`__
        The retrieved news description.
    images: `list <https://docs.python.org/3/tutorial/datastructures.html>`__
        The retrieved news thumbnails.
    """

    def __init__(self, amount: int = 3):

        if amount >= 9:
            raise TooManyRequests("Keep requests below 9 to avoid stressing the module.")

        html_page = urlopen('https://myanimelist.net/news/tag/new_anime')
        soup = BeautifulSoup(html_page, 'html.parser')

        news_container = soup.findAll('div', {'class' : 'news-unit clearfix rect'}, limit = amount)

        titles, links, description, images = [], [], [], []

        for i in news_container:
            
            text = i.findChildren("p")[0]
            a = text.find('a', href = True)
            text = a.get_text()
            
            link = a['href']

            image = i.find("img")
            image_url = image['src']

            desc = i.findChildren("div", {'class' : 'text'})[0]

            titles.append(text)
            links.append(link)
            description.append(" ".join(desc.text.split()))
            images.append(image_url)

        news = zip(titles, links, description, images)

        self.__init__ = list(news)
        
        self.titles = titles
        self.links = links
        self.description = description
        self.images = images
