from abc import ABCMeta, abstractmethod
from re import T
from typing import List, TypeVar, Type
from common.database import Database

T = TypeVar('T', bound='Model')


class Model(metaclass=ABCMeta):

    @abstractmethod
    def convert_data_to_json(self, data):
        """
        Convert data to json
        """
        raise NotImplementedError

    def save_to_database(self):
        """
        Saves the item to the database.
        """
        Database.update(self.collection, {
                        "_id": self._id}, self.convert_data_to_json())

    def remove_from_database(self):
        """
        Removes the item from the database.
        """
        Database.remove(self.collection, {"_id": self._id})

    @classmethod
    def all(cls: Type[T]) -> List[T]:
        """
        Returns all items from the database.
        """
        data_from_db = Database.find(cls.collection, {})
        return [cls(**data) for data in data_from_db]

    @classmethod
    def get_by_id(cls: Type[T], _id: str) -> T:
        """
        Returns the item from the database by id.
        """
        data_from_db = Database.find_one(cls.collection, {"_id": _id})
        return cls(**data_from_db)

    @classmethod
    def find_one_by(cls: Type[T], attribute: str, value: str) -> T:
        """
        Returns the item from the database by attribute.
        """
        data_from_db = Database.find_one(cls.collection, {attribute: value})
        return cls(**data_from_db)

    @classmethod
    def find_many_by(cls: Type[T], attribute: str, value: str) -> List[T]:
        """
        Returns the items from the database by attribute.
        """
        data_from_db = Database.find(cls.collection, {attribute: value})
        return [cls(**data) for data in data_from_db]
