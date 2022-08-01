import json
import yaml
from yaml.loader import SafeLoader

def test_open_config_file():
    with open('config.yml') as configuration:
        data = yaml.load(configuration, Loader=yaml.FullLoader)
    QUEUE = data['QUEUE']
    assert QUEUE == 'BS_exercise'

def test_JSON_file():
    with open('config.yml') as configuration:
        data = yaml.load(configuration, Loader=yaml.FullLoader)
    FILE = data['FILE_PATH']
    with open(FILE, 'r') as f:
        json_object = f.read()
    try:
        json_string = json.loads(json_object)
    except ValueError as e:
        return False
    assert True

