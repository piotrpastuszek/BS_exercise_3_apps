import yaml

def test_open_config_file():
    with open('config.yml') as configuration:
        data = yaml.load(configuration, Loader=yaml.FullLoader)
    PORT = data['PORT']
    assert PORT == '6379'