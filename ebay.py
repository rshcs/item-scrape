from bs4 import BeautifulSoup
import requests
import lxml

class Ebay:
    def __init__(self, url):
        self.url = url 
        self.web_resourse = requests.get(url)
        self.soup = BeautifulSoup(self.web_resourse.text, 'lxml')

    def get_title(self):
        title = self.soup.title.text
        title_space_loc = title.find("  |")
        return title[:title_space_loc]

    def get_seller(self):
        return self.soup.find('span', class_='mbg-nw').text

    def get_price(self):
        return self.soup.find('span', itemprop= 'price').text


if __name__ == "__main__":
    store = Ebay('https://www.ebay.com/itm/Mini-GPS-Tracker-Anti-theft-Device-Smart-Locator-Voice-Strong-Magnetic-Recorder/254283027583?hash=item3b3473147f:m:muZQsTSxg2IXpWqQxxmT_sQ&var=553752998254')

    print(store.get_title())
    print(store.get_seller())
    print(store.get_price())
