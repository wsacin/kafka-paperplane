
class DefaultStrategy:

    def __init__(self):
        self._connection = None

    def unread_notifications(self):
        raise NotImplementedError()

    def save_notification(self, notification):
        raise NotImplementedError()

    def last_notifications(self, last_n=5):
        raise NotImplementedError()

    def read_last_notifications(self, last_n=5):
        raise NotImplementedError()

    def read_one(self, offset):
        raise NotImplementedError()

    @property
    def connection(self, notification):
        raise NotImplementedError()

