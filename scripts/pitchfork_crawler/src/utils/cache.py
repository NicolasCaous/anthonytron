from os.path import isfile
import json


class CacheManager:
    def __init__(self, folder):
        self.folder = folder

    def __getitem__(self, path):
        if isfile("{}/{}".format(self.folder, path)):
            with open("{}/{}".format(self.folder, path), "r") as file:
                return json.load(file)
        else:
            return None

    def __setitem__(self, path, data):
        with open("{}/{}".format(self.folder, path), "w") as file:
            return json.dump(data, file)
