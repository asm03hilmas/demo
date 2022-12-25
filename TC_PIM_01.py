from selenium import webdriver
from selenium.webdriver.common.by import By
import time as sleep

# import pytest

import login1
from test_data import data_01


def loginadmin():
    login1.login()


def search_box(self, loginadmin):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    search_title = self.driver.find_element(
        By.XPATH, value=data_01.menu.search_menu)
    search_title.click()
    ad_vari = search_title.send_keys(data_01.key_data.search_admin)

    lists = driver.find_element(By.XPATH, value=data_01.menu.list)
    # if == lists:

    #     print("admin has visible")
    # else:
    print("NOT VISIBLE")


loginadmin()
search_box()
