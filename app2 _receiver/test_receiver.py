import yaml
from yaml.loader import SafeLoader


def test_open_config_file():
    with open('config.yml') as configuration:
        data = yaml.load(configuration, Loader=yaml.FullLoader)
    QUEUE = data['QUEUE']
    assert QUEUE == 'BS_exercise'

def test_open_config_file():
    with open('config.yml') as configuration:
        data = yaml.load(configuration, Loader=yaml.FullLoader)
    REDIS_PORT = data['REDIS_PORT']
    assert REDIS_PORT == '6379'