# Kafka Paperplane Sink

A simple implementation of a sink for storing incoming messages
on a given MongoDB server.

### Usage

Use honcho to run the server. [Honcho](http://honcho.readthedocs.io/en/latest/) is a Python port of Foreman. Honcho helps to manage procfile-based applications so that you
can run Python code under a specific environment.

Given an environment such as the one bellow:
```env
BOOTSTRAP_SERVERS=my.kafka.broker.ip1:9092,my.kafka.broker.ip2:9092
CONNECTION_URL=mongodb://localhost:27017/
COLLECTION=notifications
TOPIC=paperplane
GROUP_ID=default
DATABASE=paperplane
DEBUG=True
```

A Procfile describing the Python application that runs with the
environment above would be:

```procfile
sink: python3 sink.py
```

Then, to run the application, specify the env file and the procfile:

```bash
$ honcho start -e .env -f Procfile
```
