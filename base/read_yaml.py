import os

import yaml


class ReadYaml():

    def __init__(self, filename):
        self.filename = os.getcwd() + os.sep + "data" + os.sep + filename

    # os.getcwd() + os.sep + "data" + os.sep +
    def read_yaml(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            return yaml.load(f)

if __name__ == '__main__':
    list = [ ]
    for i in ReadYaml("../data/address_data.yaml").read_yaml().values():
        list.append((i.get("name"), i.get("phone"), i.get("province"), i.get("city"), i.get("area"), i.get("detail"), i.get("code")))
    print(list)