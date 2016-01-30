import json
import os

engines = filter(lambda name: name.endswith('json'),
                 os.listdir(os.path.dirname(__file__)))

def get_config(engine_name):
    root_path = os.path.dirname(__file__)
    with open(os.path.join(root_path, engine_name)) as file_e:
        return json.load(file_e)
