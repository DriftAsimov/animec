from bs4 import BeautifulSoup
from urllib.request import urlopen

class aninews:

    def __init__(self, amount: int = 3):

        if amount >= 15:
            print("Keep requests below 15 to avoid stressing the API.")
            return

        html_page = urlopen('https://myanimelist.net/news')
        soup = BeautifulSoup(html_page, 'html.parser')

        news_container = soup.findAll('div', {'class' : 'news-unit clearfix rect'})
        stripped_list = news_container[:amount]

        titles, links, description = [], [], []

        for i in stripped_list:
            
            text = i.findChildren("p")[0]
            a = text.find('a', href = True)
            link = a['href']
            text = a.get_text()

            desc = i.findChildren("div", {'class' : 'text'})[0]

            titles.append(text)
            links.append(link)
            description.append(" ".join(desc.text.split()))

        news = zip(titles, links, description)

        self.news = list(news)
        self.titles = titles
        self.links = links
        self.description = description
