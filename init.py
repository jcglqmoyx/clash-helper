import json
from functools import cache


@cache
def read_configuration():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config
