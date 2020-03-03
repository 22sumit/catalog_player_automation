import logging

from selenium.webdriver.common.by import By
from PageObject.BroadcastOfferingPage import BroadcastOfferingPage
from PageObject.StbConfigPage import StbConfigPage
from PageObject.CatalogPage import CatalogPage

log = logging.getLogger(__name__)

class HomePage:

    def __init__(self, edriver):
        self.driver = edriver

    __broadcast_menu = (By.ID, "tvgcmBroadcastOfferingsMainMenu")
    __list_Broadcast_Offerings_menu = (By.XPATH, "//a[contains(text(),'List Broadcast Offerings')]")
    __add_Broadcast_Offerings_menu = (By.XPATH, "//a[contains(text(),'Add Broadcast Offering')]")
    __stbConfig_menu = (By.ID, "tvgcmStbConfigMainMenu")
    __list_stbConfig_menu = (By.XPATH, "//a[contains(text(),'List STB Configs')]")
    __add_stbConfig_menu = (By.XPATH, "//a[contains(text(),'Add STB Config')]")
    __catalog_menu = (By.XPATH, "//a[contains(text(),'Catalog')]")
    __list_category = (By.XPATH, "//a[contains(text(),'List Categories')]")
    __add_category = (By.XPATH, "//a[contains(text(),'Add Category')]")


    def goto_list_stbConfig_page(self):
        driver = self.driver
        driver.find_element(*HomePage.__stbConfig_menu).click()
        driver.find_element(*HomePage.__list_stbConfig_menu).click()
        log.info("STB Configuration list page opened")
        STB_CONFIG_LIST_PAGE = StbConfigPage(driver)
        return STB_CONFIG_LIST_PAGE

    def goto_add_stbConfig_page(self):
        driver=self.driver
        driver.find_element(*HomePage.__stbConfig_menu).click()
        driver.find_element(*HomePage.__add_stbConfig_menu).click()
        log.info("Add STB Configuration page opened")
        STB_CONFIG_ADD_PAGE = StbConfigPage(driver)
        return STB_CONFIG_ADD_PAGE

    def goto_list_broadcast_offering_page(self):
        driver = self.driver
        driver.find_element(*HomePage.__broadcast_menu).click()
        driver.find_element(*HomePage.__list_Broadcast_Offerings_menu).click()
        log.info("Broadcast Offering list page opened")
        BROADCAST_OFFERING_LIST_PAGE = BroadcastOfferingPage(driver)
        return BROADCAST_OFFERING_LIST_PAGE


    def goto_add_broadcast_offering_page(self):
        driver=self.driver
        driver.find_element(*HomePage.__broadcast_menu).click()
        driver.find_element(*HomePage.__add_Broadcast_Offerings_menu).click()
        log.info("Add Broadcast Offering page opened")
        BROADCAST_OFFERING_ADD_PAGE = BroadcastOfferingPage(driver)
        return BROADCAST_OFFERING_ADD_PAGE

    def goto_list_categories(self):
        driver = self.driver
        driver.find_element(*HomePage.__catalog_menu).click()
        driver.find_element(*HomePage.__list_category).click()
        log.info("Category list page opened")

    def goto_add_category(self):
        driver=self.driver
        driver.find_element(*HomePage.__catalog_menu).click()
        driver.find_element(*HomePage.__add_category).click()
        log.info("Add Category page opened")
        CATALOG_PAGE = CatalogPage(driver)
        return CATALOG_PAGE