from .default import DefaultStrategy
import redis


class RedisStrategy(DefaultStrategy):

    def __init__(self, host='localhost', port=6379, db=0):
        self._host = host
        self._port = port
        self._db = db
        self._connection = None

    @property
    def connection(self):
        if not self._connection:
            self._connection = redis.StrictRedis(
                    self._host, self._port, self._db)
        return self._connection

    def save_notification(self, notification):
        self.connection.set(notification['timestamp'], notification)
