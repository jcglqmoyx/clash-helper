import re

import bs4
import requests

from init import read_configuration
from util import generate_username


def send_verification_code_to_email(email):
    config = read_configuration()
    url = config["api"]["clash-nodes"]['gou']['send-email']
    res = requests.post(url, json={"email": email})
    print(res.json()['msg'])


def extract_verification_code_from_email(msg):
    match = re.search(r"\d{6}", msg)
    verification_code = match.group(0)
    return verification_code


def register(email, psd, verification_code):
    config = read_configuration()
    url = config["api"]["clash-nodes"]['gou']['registration']
    res = requests.post(url, json={
        'email': email,
        'name': email,
        'passwd': psd,
        'repasswd': psd,
        'wechat': generate_username(),
        'imtype': 1,
        'code': 0,
        'emailcode': verification_code,
    })
    print(res.json()['msg'])


def login(email, psd):
    config = read_configuration()
    url = config["api"]["clash-nodes"]['gou']['login']
    res = requests.post(url, json={
        'email': email,
        'passwd': psd,
    })
    return res.cookies


def get_subscription_link(cookies):
    config = read_configuration()
    url = config["api"]["clash-nodes"]['gou']['profile']
    res = requests.get(url, cookies=cookies).text
    soap = bs4.BeautifulSoup(res, 'html.parser')
    link = soap.select('#all_v2ray_client > div:nth-child(13) > input')[0]['value']
    return link
