import random
import time

import requests

from init import read_configuration
from util import generate_username, generate_password


def get_domains():
    config = read_configuration()
    url = config["api"]["email"]["domain"]
    res = requests.get(url)
    return res.json()['hydra:member']


def register():
    domains = get_domains()
    domain = domains[random.randint(0, len(domains) - 1)]['domain']
    config = read_configuration()
    url = config["api"]["email"]["registration"]
    email, password = generate_username() + '@' + domain, generate_password()
    requests.post(url, json={"address": email, "password": password})
    print(f"Email: {email}\nPassword: {password}")
    return email, password


def login(email, password):
    config = read_configuration()
    url = config["api"]["email"]["token"]
    res = requests.post(url, json={"address": email, "password": password})
    return res.json()['token']


def get_first_message(token):
    config = read_configuration()
    url = config["api"]["email"]["message"]
    while True:
        res = requests.get(url, headers={'Authorization': f'Bearer {token}'})
        if res.json()['hydra:member']:
            break
        time.sleep(1)
    return res.json()['hydra:member'][0]['intro']
