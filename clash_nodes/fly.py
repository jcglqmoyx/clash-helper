import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from init import read_configuration
from util import random_email, generate_password


class Fly:
    def __init__(self):
        config = read_configuration()
        chromedriver_path = config["selenium"]["chrome-driver-path"]
        brave_browser_path = config["selenium"]["brave-browser-path"]
        options = Options()
        options.binary_location = brave_browser_path
        options.add_argument("--disable-extensions")
        options.add_argument("profile-directory=Default")
        service = Service(chromedriver_path)
        self.driver = webdriver.Chrome(service=service, options=options)

    def __del__(self):
        self.driver.quit()

    def register(self):
        config = read_configuration()
        self.driver.get(config["api"]['clash-nodes']["fly"]["registration"])
        self.driver.set_window_size(1496, 848)
        self.driver.find_element(By.ID, "input-1").click()
        self.driver.find_element(By.ID, "input-1").send_keys(random_email())
        self.driver.find_element(By.ID, "input-3").click()
        self.driver.find_element(By.ID, "input-3").send_keys(generate_password())
        self.driver.find_element(By.ID, "input-7").click()
        time.sleep(120)
