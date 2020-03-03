import logging

from selenium.webdriver.common.by import By
from libs import config

log = logging.getLogger(__name__)

class LoginPage():

    def __init__(self, edriver):
        self.driver = edriver

    __username_text_box = (By.NAME, "j_username")
    __password_text_box = (By.NAME, "j_password")
    __login_button = (By.XPATH, "//input[@value='Login']")
    __logout_button = (By.XPATH, "//a[contains(text(),'Logout')]")

    url = config.get_default("url")
    username = config.get_default("username")
    password = config.get_default("password")

    def login(self):
        driver=self.driver
        driver.get(self.url)
        driver.find_element(*LoginPage.__username_text_box).send_keys(self.username)
        driver.find_element(*LoginPage.__password_text_box).send_keys(self.password)
        driver.find_element(*LoginPage.__login_button).click()

    def assert_title(self):
        assert self.driver.title == "TVGCM: Catalog Player Status"
        log.info("Login is Successful !!")

    def logout(self):
        driver=self.driver
        driver.find_element(*LoginPage.__logout_button).click()
        log.info("Successfully Logged Out!!")