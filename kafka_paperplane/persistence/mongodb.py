from .default import DefaultStrategy
import pymongo


class MongoStrategy(DefaultStrategy):

    def __init__(
            self, connection_url='mongodb://localhost:27017',
            database='paperplane', collection='notifications'):
        self._connection_url = connection_url
        self._collection_string = collection
        self._database_string = database
        self._collection = None
        self._database = None
        self._connection = None
        self._check_for_index()

    @property
    def connection(self):
        if not self._connection:
            self._connection = pymongo.MongoClient(
                    self._connection_url, w=0)
        return self._connection

    @property
    def database(self):
        if not self._database:
            self._database = self.connection[self._database_string]
        return self._database

    @property
    def collection(self):
        if not self._collection:
            self._collection = self.database[self._collection_string]
        return self._collection

    def save_notification(self, notification):
        notification['read'] = False
        return self.collection.insert_one(notification)

    def last_notifications(self, last_n=5):
        return self.collection.find().sort(
                'offset', pymongo.DESCENDING)[:last_n]

    def unread_notifications(self, last_n=None):
        if last_n:
            return self.collection.find({'read': False}).sort(
                    'offset', pymongo.DESCENDING)[:last_n]
        else:
            return self.collection.find({'read': False}).sort(
                    'offset', pymongo.DESCENDING)

    def read_notifications(self, last_n=None):
        unread = self.unread_notifications(last_n=last_n)
        for notif in unread:
            self.collection.update_one(
                    {'offset': notif['offset']},
                    {'$set': {'read': True}})
        return True

    def _check_for_index(self):
        if 'offset_-1' in self.collection.index_information():
            return True
        else:
            self.collection.create_index(
                    [('offset', pymongo.DESCENDING)]
                )
            return self.collection.index_information()
