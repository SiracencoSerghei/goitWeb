import json
import yaml

class Storage:
    def get_value(self, key):
        raise NotImplementedError

class JSONStorage(Storage):
    def __init__(self, filename):
        self.filename = filename

    def get_value(self, key):
        with open(self.filename, 'r') as fh:
            data = json.load(fh)
            return data.get(key, None)


class YamlStorage(Storage):
    def __init__(self, filename):
        self.filename = filename

    def get_value(self, key):
        with open(self.filename, 'r') as fh:
            data = yaml.load(fh, Loader=yaml.FullLoader)
            return data.get(key, None)

