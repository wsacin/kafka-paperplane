
# Kafka Paperplane

Dockerized Apache Kafka and API (PaperPlane) to abstract
Kafka's Consumer and Producer into one wrapper in
a notificaiton system fashion.

## Client API

### Usage

```python
from kafka_paperplane import PaperPlane


notifier = PaperPlane(
        broker_address='my.broker.ip.addr:9092',
        receive_from=[],
            # List of topics to subscribe to.
            # [] if client will only send.
        send_to=[],
            # List of target topics for messages sent from
            # this notifier. [] if client will only receive.
        group_id='',
            # (Optional) Notifiers with the the same id will receive
            # notifications in a round-robin manner.
        database_strategy=None,
            # (Optional) Object that dictates what
            # storage backend which the notifications
            # will be persisted. If None, PaperPlane will
            # not persist.
    )


# Send notifications for registered topics.
# Registered message types:
#    ALERT, WARNING, TASK, LOG
notifier.send_notification('hello', 'ALERT')


# Send notifications for arbitrary topics.
notifier.send_notification('hello', 'ALERT', topic='foo')


# Listen for notifications on registered topics
for notification in notifier.poll_notifications():
    print(notification)


# Listen for raw Kafka messages (ConsumerRecord)
for notification in notifier.poll_raw_messages():
    print(notification)
```


#### Persistence

```python
from kafka_paperplane import PaperPlane
from kafka_paperplane.persistence import MongoStrategy


notifier = PaperPlane(
        broker_address='my.broker.ip.addr:9092',
        receive_from=['foo'],
        send_to=['bar'],
        database_strategy=MongoStrategy(),
            # MongoStrategy with default configuration. this
            # will create connections with a local instance
            # of MongoDB.
    )
```
