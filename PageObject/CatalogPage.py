import datetime
import logging

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from libs import config
from libs.BaseClass import BaseClass
from utils.mongodbutils import connect_to_db, findone

log = logging.getLogger(__name__)

class CatalogPage:

    def __init__(self, edriver):
        self.driver = edriver

    navigationId = config.get_default("navigationId")
    __categoryId = (By.XPATH, "//input[@id='category']")
    __navigationId = (By.XPATH, "//input[@id='navigation']")
    __hotLaunchSourceId = (By.XPATH, "//input[@id='hotlaunchsourceId']")
    __save_button = (By.XPATH, "//input[@value='Save']")
    __category_success_msg = (By.XPATH, "//p[contains(text(),'Category added successfully.')]")
    __publish_button = (By.XPATH, "//div[@class='publish']//input")
    __publish_successful_msg = (By.XPATH, "//p[contains(text(),'Categories published successfully.')]")
    __duplicate_hotLaunchSourceId_error_msg = (By.XPATH, "//li[contains(text(),'The HotLauchSourceID you are trying to add already')]")
    __delete_button = (By.XPATH, "//input[@class='delete']")
    __delete_successful_msg = (By.XPATH, "//div/p[1][@class='message success']")

    __table = (By.XPATH, "//table[@class='list']")

    def add_and_publish_category(self,hlsId):
        driver=self.driver
        date = datetime.datetime.now()
        dt = date.strftime("%Y%m%d%H%M%S")
        categoryId = "Category" + dt
        log.info("Adding categoryId {} and hotLaunchSourceIds {}".format(categoryId, hlsId))
        driver.find_element(*CatalogPage.__categoryId).send_keys(categoryId)
        driver.find_element(*CatalogPage.__navigationId).send_keys(self.navigationId)
        driver.find_element(*CatalogPage.__hotLaunchSourceId).send_keys(hlsId)
        driver.find_element(*CatalogPage.__save_button).click()
        try:
            category_success_msg=driver.find_element(*CatalogPage.__category_success_msg)
            category_success_msg.is_displayed()
            log.info(driver.find_element(*CatalogPage.__category_success_msg).text)
            __checkbox = "//td[contains(text(),'" + hlsId + "')]//preceding::input[1]"
            driver.find_element_by_xpath(__checkbox).click()
            driver.find_element(*CatalogPage.__publish_button).click()
            BaseClass.alert_accept(self)
            driver.find_element(*CatalogPage.__publish_successful_msg).is_displayed()
            log.error(driver.find_element(*CatalogPage.__publish_successful_msg).text)
        except NoSuchElementException:
            duplicate_hotLaunchSourceId_error_msg = driver.find_element(*CatalogPage.__duplicate_hotLaunchSourceId_error_msg)
            duplicate_hotLaunchSourceId_error_msg.is_displayed()
            log.info(driver.find_element(*CatalogPage.__duplicate_hotLaunchSourceId_error_msg).text)
            log.info("Category Not added !!")

    def delete_category(self,hlsId):
        driver=self.driver
        __delete_hotLaunchSource="//td[contains(text(),'" + hlsId + "')]//preceding::input[1]"
        driver.find_element_by_xpath(__delete_hotLaunchSource).click()
        driver.find_element(*CatalogPage.__delete_button).click()
        BaseClass.alert_accept(self)
        driver.find_element(*CatalogPage.__delete_successful_msg).is_displayed()
        log.info(driver.find_element(*CatalogPage.__delete_successful_msg).text)

    def list_hotLaunchSource_Ids(self):
        ''' Fetch the list of available categories '''
        driver=self.driver
        table=driver.find_element(*CatalogPage.__table)
        rowCount = BaseClass.getWebTableRowCount(self, table)
        hl_list = []
        for i in range(2, rowCount + 1):
            hl_xpath = "//table[1]/tbody[1]/tr[" + str(i) + "]/td[4]"
            hl_list.append(driver.find_element_by_xpath(hl_xpath).text)
        str1 = ','.join(hl_list)
        hls = list(str1.split(","))
        log.info("List of available hotLaunchSourceIds :", hls)
        # return hls