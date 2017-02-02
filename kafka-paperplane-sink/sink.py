from kafka_paperplane.persistence import MongoStrategy
from kafka_paperplane import PaperPlane
import settings
import logging


logger = logging.getLogger(name='{} sink'.format(settings.TOPIC))
log_level = logging.DEBUG if settings.DEBUG else logging.INFO
logger.setLevel(log_level)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
handler.setLevel(log_level)
logger.addHandler(handler)


logger.info('servers: {}'.format(settings.BOOTSTRAP_SERVERS))
logger.info('mongo: {}'.format(settings.CONNECTION_URL))
logger.info('topic: {}'.format(settings.TOPIC))
logger.info('database: {}'.format(settings.DATABASE))
logger.info('collection: {}'.format(settings.COLLECTION))

mongo_strategy = MongoStrategy(
        connection_url=settings.CONNECTION_URL,
        database=settings.DATABASE,
        collection=settings.COLLECTION
    )

sink = PaperPlane(
        bootstrap_servers=settings.BOOTSTRAP_SERVERS,
        receive_from=[settings.TOPIC],
        group_id=settings.GROUP_ID,
        send_to=[],
        database_strategy=mongo_strategy,
        )


for msg in sink.poll_raw_messages():
    logger.info('received message ({}) - {}'.format(msg.offset, msg.value))
