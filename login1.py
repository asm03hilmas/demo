from selenium import webdriver
from selenium.webdriver.common.by import By
import time as sleep
from selenium.webdriver.common.action_chains import ActionChains


def login1(self):

    driver = webdriver.Chrome()
    driver.get(
        "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    driver.maximize_window()
    driver.implicitly_wait(10)
    # get the  input user lodin data
    username = 'Admin'
    password = 'admin123'

    # location of elements data

    user_name = 'username'
    password_name = 'password'
    login_class = "//button[normalize-space()='Login']"

    # find the title of website name
    title = self.driver.title

    print(title)

    self.driver.find_element(By.NAME, value=user_name).send_keys(username)
    self.driver.find_element(
        By.NAME, value=password_name).send_keys(password)
    loginbtn = self.driver.find_element(By.XPATH, login_class).click()

    # def admin():
    #     s_box = selfself.driver.find_element(
    #         By.XPATH, value="//input[@placeholder='Search']")
    #     s_box.click
    #     s_box.send_keys("Admin")



