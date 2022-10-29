import os
from decouple import config

driver_aws = 'postgresql+psycopg2://'
driver_local = 'postgresql://'


uri = os.getenv('SQLALCHEMY_DATABASE_URI',
                driver_local \
                + config('POSTGRES_USER') \
                + ':' \
                + config('POSTGRES_PASSWORD') \
                +'@'\
                + config('POSTGRES_HOST') \
                + '/' \
                + config('POSTGRES_DB'))


class Config(object):
    TESTING = False
    DEVICE_HOST = "http://devices:3040"
    SQLALCHEMY_DATABASE_URI = uri
    JWT_SECRET_KEY = 'secret-word'
    PROPAGATE_EXCEPTIONS = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False