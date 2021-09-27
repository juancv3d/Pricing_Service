from typing import Dict
import re
import requests
from uuid import uuid4
from bs4 import BeautifulSoup
from common.database import Database


class Item:
    def __init__(self, url: str, tag: str, query: Dict, _id: str = None):
        self.url = url
        self.tag = tag
        self.query = query
        self.price = None
        self.collection = 'items'
        self._id = _id or uuid4().hex

    def __repr__(self):
        """
        returns the object in a string format.
        """
        return f'<Item {self.url}>'

    def convert_data_to_json(self):
        """
        Converts the data to a json format.

        Returns:
            json (dict): The data in json format.
        """
        return {
            '_id': self._id,
            'url': self.url,
            'tag': self.tag,
            'query': self.query
        }

    def get_price(self):
        """
        Get the price of the item by scraping the page. After getting the price, 
        it will delete the dots and commas from the price to make it easier to convert it to float.

        Returns:
            price (float): The price of the item.
        """
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        element = soup.find(self.tag, self.query)
        string_price = element.text.strip()
        pattern = re.compile(r'\d+[\.,]?\d+[\.,]\d+')
        self.price = float(pattern.findall(string_price)[0].replace(
            ',', '').replace('.', ''))
        return self.price

    def save_to_database(self):
        """
        Saves the item to the database.
        """
        Database.insert(self.collection, self.convert_data_to_json())

    @classmethod
    def all(cls):
        """
        Returns all the items from the database.

        Returns:
            items (list): All the items from the database.
        """
        return [cls(**item) for item in Database.find('items', {})]
