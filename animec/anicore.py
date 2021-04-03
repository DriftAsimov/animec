from bs4 import BeautifulSoup
from urllib.request import urlopen

class anime:

    def __init__(self, query):

        if " " in query:
            query = query.replace(" ", "%20")

        to_open = f"https://myanimelist.net/anime.php?q={query}"

        try:
            html_page = urlopen(to_open)
        except UnicodeEncodeError:
            encoded_url = to_open.encode('ascii','ignore')
            html_page = urlopen(str(encoded_url))
        
        soup = BeautifulSoup(html_page, 'html.parser')

        anime_div = soup.find("td", {'class': 'borderClass bgColor0'})
        url = anime_div.find("a", href = True)

        self.url = url['href']

    def recommend(self, amount: int = 5):

        if amount >= 10:
            print("Keep requests below 10 to avoid stressing the API.")
            return

        anime_page = urlopen(f"{self.url}/userrecs")
        soup = BeautifulSoup(anime_page, 'html.parser')

        headers = soup.findAll("strong")

        recommendations = []

        for i in headers:
            recommendations.append(i.get_text())

        ri = [i for i in recommendations if not i.isdigit()]  
        ri.pop(0)

        return ri[:amount]