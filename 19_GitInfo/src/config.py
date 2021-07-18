class Config(object):
    TESTING = False

class ProductionConfig(Config):
    DEBUG = False
    JSON_SORT_KEYS = False
    SECRET_KEY = b'\xb0K\xb4\xb2\xa5\x91\xae\x99\xe9e\x1d\xff\xcf\x9d\xb3\x9a'


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = b'\xb0K\xb4\xb2\xa5\x91\xae\x99\xe9e\x1d\xff\xcf\x9d\xb3\x9a'


class TestingConfig(Config):
    DEBUG = True
    SECRET_KEY = b'\xb0K\xb4\xb2\xa5\x91\xae\x99\xe9e\x1d\xff\xcf\x9d\xb3\x9a'
    TESTING = True
