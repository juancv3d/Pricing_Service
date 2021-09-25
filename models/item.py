import re
import requests
from bs4 import BeautifulSoup

URL = 'https://www.linio.com.co/p/imac-con-pantalla-retina-4k-215-intel-core-i3-1tb-mrt32e-a-apple-jr3hnd?qid=5ed7ee35c9d4a4afb3fe1cf00c2f97f1&oid=AP039EL1L1ECHLCO&position=1&sku=AP039EL1L1ECHLCO'
TAG_NAME = 'span'
QUERY = {'class': 'price-main-md'}


class Item:
    def __init__(self, url, tag, query):
        self.url = url
        self.tag = tag
        self.query = query

    def get_price(self):
        """
        Get the price of the item by scraping the page. After getting the price, 
        it will delete the dots and commas from the price to make it easier to convert it to float.

        Returns:
            price (str): The price of the item.
        """
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        element = soup.find(self.tag, self.query)
        string_price = element.text.strip()
        pattern = re.compile(r'\d+[\.,]?\d+[\.,]\d+')
        price = pattern.findall(string_price)[0].replace(
            ',', '').replace('.', '')
        return float(price)


if __name__ == '__main__':
    item = Item(URL, TAG_NAME, QUERY)
    print(item.get_price())
