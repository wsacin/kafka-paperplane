from .default import DefaultStrategy
from redis import StrictRedis


class RedisStrategy(DefaultStrategy):

    def __init__(self, host='localhost', port=6379, db=0):
        self._host = host
        self._port = port
        self._db = db
        super().__init__()

    @property
    def connection(self):
        if not self._connection:
            self._connection = StrictRedis(
                    self._host, self._port, self._db)
        return self._connection

    def save_notification(self, notification):
        self.connection.set(notification['timestamp'], notification)
