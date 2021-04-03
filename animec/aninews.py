from bs4 import BeautifulSoup
from urllib.request import urlopen

class aninews:

    def __init__(self, amount: int = 3):

        if amount >= 15:
            print("Keep requests below 15 to avoid stressing the API.")
            return

        html_page = urlopen('https://myanimelist.net/news/tag/new_anime')
        soup = BeautifulSoup(html_page, 'html.parser')

        news_container = soup.findAll('div', {'class' : 'news-unit clearfix rect'})
        stripped_list = news_container[:amount]

        titles, links, description, images = [], [], [], []

        for i in stripped_list:
            
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

        self.news = list(news)
        
        self.titles = titles
        self.links = links
        self.description = description
        self.images = images
