from typing import Dict, List
from common.database import Database
from models.item import Item
from uuid import uuid4


class Alert:

    collection = 'alerts'

    def __init__(self, item_id: str, price_limit: float, _id: str = None):
        self.item_id = item_id
        self.item = Item.get_by_id(item_id)
        self.price_limit = price_limit
        self.collection = 'alerts'
        self._id = _id or uuid4().hex

    def convert_data_to_json(self) -> Dict:
        """
        Converts the data to a json format.

        Returns:
            json (dict): The data in json format.
        """
        return {
            '_id': self._id,
            'item_id': self.item_id,
            'price_limit': self.price_limit
        }

    def get_item_price(self) -> float:
        """
        Gets the item price.

        Returns:
            float: The item price.
        """
        self.item.get_price()
        return self.item.price

    def save_to_database(self):
        """
        Saves the item to the database.
        """
        Database.insert(self.collection, self.convert_data_to_json())

    @classmethod
    def all(cls) -> List:
        """
        Gets all the alerts.

        Returns:
            List: The list of all alerts.
        """
        return [cls(**alerts) for alerts in Database.find(cls.collection, {})]
