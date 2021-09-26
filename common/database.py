from typing import Dict
from dotenv import load_dotenv
import os
from pymongo import MongoClient


load_dotenv()


class Database:
    client = MongoClient(os.getenv("MONGODB_URI"))
    DATABASE = client.pricing_service

    @staticmethod
    def insert(collection: str, data: Dict):
        Database.DATABASE[collection].insert(data)
