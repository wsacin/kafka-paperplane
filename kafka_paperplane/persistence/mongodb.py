from .default import DefaultStrategy
from pymongo import MongoClient


class MongoStrategy(DefaultStrategy):

    def __init__(
            self, connection_url='mongodb://localhost:27017',
            database='paperplane', collection='notifications'):
        self._connection_url = connection_url
        self._database = database
        self._collection = collection
        super().__init__()

    @property
    def connection(self):
        if not self._connection:
            self._connection = MongoClient(self._connection_url)
        return self._connection

    def save_notification(self, notification):
        collection = self.connection[self._database][self._collection]
        collection.insert_one(notification)
