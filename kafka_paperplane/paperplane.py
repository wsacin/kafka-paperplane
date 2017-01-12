
from kafka import KafkaProducer, KafkaConsumer
from .notification import Notification
import json


class PaperPlane(object):
    """
    Class for generating communicating actors of
    a notification system using Apache Kafka.
    """
    def __init__(
            self, broker_address, receive_from,
            send_to, group_id='', database_strategy=None):
        self._broker_address = broker_address
        self._send_to = send_to
        self._receive_from = receive_from
        self._group_id = group_id
        self._database_strategy = database_strategy
        self._consumer = None
        self._producer = None

    def poll_notifications(self):
        for msg in self.consumer:
            data = json.loads(msg.value.decode('utf-8'))
            if self._database_strategy:
                self._database_strategy.save_notification(data)
            yield data

    def poll_raw_messages(self):
        for msg in self.consumer:
            yield msg

    def send_notification(
            self, message, message_type, topic=''):

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
        params['bootstrap_servers'] = [self._broker_address]

        if not self._consumer:
            self._consumer = KafkaConsumer(**params)
            for topic in self._receive_from:
                self._consumer.subscribe(topic)
        return self._consumer

    @property
    def producer(self):
        if not self._producer:
            self._producer = KafkaProducer(
                    bootstrap_servers=[self._broker_address],
                )
        return self._producer
