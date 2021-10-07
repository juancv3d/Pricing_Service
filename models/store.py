import re
from uuid import uuid4
from typing import Dict
from models.model import Model


class Store(Model):
    collection = "store"

    def __init__(self, name: str, url_prefix: str, tag_name: str, query: Dict, _id: str = None):
        self.name = name
        self.url_prefix = url_prefix
        self.tag_name = tag_name
        self.query = query
        self._id = _id or uuid4().hex

    def convert_data_to_json(self):
        return {
            'name': self.name,
            'url_prefix': self.url_prefix,
            'tag_name': self.tag_name,
            'query': self.query,
            '_id': self._id
        }

    @classmethod
    def get_by_name(cls, store_name: str) -> "Store":
        return cls.find_one_by('name', store_name)

    @classmethod
    def get_by_url_prefix(cls, url_prefix: str) -> "Store":
        # url_regex will be used to match the url_prefix in the database and
        # return the store object if it matches the url_prefix
        url_regex = {"$regex": "^{}".format(url_prefix)}
        return cls.find_one_by('url_prefix', url_regex)

    @classmethod
    def find_by_url(cls, url: str) -> "Store":
        """
        Return a store from a url like "http://www.johnlewis.com/item/sdfsdfdsfsd.html"
        """
        pattern = re.compile(r"(https?://.*?/)")
        match = pattern.search(url)
        url_prefix = match.group(1)
        return cls.get_by_url_prefix(url_prefix)
