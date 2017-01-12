
class DefaultStrategy:

    def __init__(self):
        self._connection = None

    def save_notification(self, notification):
        raise NotImplementedError()

    @property
    def connection(self, notification):
        raise NotImplementedError()

