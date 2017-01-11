
class DefaultStrategy(object):

    def __init__(self, url):
        self._url = url

    @property
    def connection(self, notification):
        raise NotImplementedError()

    def save_notification(self, notification):
        raise NotImplementedError()


class MongoDB(DefaultStrategy):

    def __init__(self, url):
        super().__init__(url)
