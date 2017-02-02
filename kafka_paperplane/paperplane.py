
from kafka import KafkaProducer, KafkaConsumer
from .notification import Notification
from datetime import datetime as dt
from datetime import timezone as tz
import yajl


class PaperPlane(object):
    """
    Class for generating communicating actors of
    a notification system using Apache Kafka.
    """
    def __init__(
            self, bootstrap_servers, receive_from,
            send_to, group_id='', auto_offset_reset='',
            database_strategy=None):
        self._auto_offset_reset = auto_offset_reset
        self._bootstrap_servers = bootstrap_servers
        self._database_strategy = database_strategy
        self._receive_from = receive_from
        self._group_id = group_id
        self._send_to = send_to
        self._consumer = None
        self._producer = None

    def poll_notifications(self):
        for msg in self.consumer:
            data = yajl.loads(msg.value.decode('utf-8'))
            data['offset'] = msg.offset
            if self._database_strategy:
                data['timestamp'] = msg.timestamp
                self._database_strategy.save_notification(data)
            data['timestamp'] = dt.fromtimestamp(
                    msg.timestamp / 1000, tz.utc)
            yield data

    def poll_raw_messages(self):
        for msg in self.consumer:
            if self._database_strategy:
                data = {
                    'timestamp': dt.fromtimestamp(
                        msg.timestamp / 1000, tz.utc),
                    'offset': msg.offset,
                    'message': msg.value.decode('utf-8')
                }
                self._database_strategy.save_notification(data)
            yield msg

    def send_notification(self, message, message_type, topic=''):

        payload = Notification.create(message, message_type)

        if topic:
            self.producer.send(topic, message)
        else:
            for topic in self._send_to:
                self.producer.send(topic, payload)

    @property
    def consumer(self):
        params = {}
        if self._group_id:
            params['group_id'] = self._group_id
        if self._auto_offset_reset:
            params['auto_offset_reset'] = self._auto_offset_reset
        params['bootstrap_servers'] = self._bootstrap_servers

        if not self._consumer:
            self._consumer = KafkaConsumer(**params)
            self._consumer.subscribe(self._receive_from)
        return self._consumer

    @property
    def producer(self):
        if not self._producer:
            self._producer = KafkaProducer(
                    bootstrap_servers=self._bootstrap_servers,
                )
        return self._producer
