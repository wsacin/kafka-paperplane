
class DefaultStrategy:

    def __init__(self, connection_url):
        self._url = connection_url

    def save_notification(self, notification):
        raise NotImplementedError()

    @property
    def connection(self, notification):
        raise NotImplementedError()

