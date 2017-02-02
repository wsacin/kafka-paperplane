from decouple import config


BOOTSTRAP_SERVERS = config('BOOTSTRAP_SERVERS').split(',')
CONNECTION_URL = config('CONNECTION_URL')
DEBUG = config('DEBUG', cast=bool)
COLLECTION = config('COLLECTION')
DATABASE = config('DATABASE')
GROUP_ID = config('GROUP_ID')
TOPIC = config('TOPIC')
