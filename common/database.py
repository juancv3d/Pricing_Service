from typing import Dict
from dotenv import load_dotenv
import os
from pymongo import MongoClient, cursor


load_dotenv()


class Database:
    client = MongoClient(os.getenv("MONGODB_URI"))
    DATABASE = client.pricing_service

    @staticmethod
    def insert(collection: str, data: Dict):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection: str, query: Dict) -> cursor:
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection: str, query: Dict) -> Dict:
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection: str, query: Dict, data: Dict):
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection: str, query: Dict):
        Database.DATABASE[collection].remove(query)
