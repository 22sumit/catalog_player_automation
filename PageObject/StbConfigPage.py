import logging
import sys
import time

from selenium.webdriver.common.by import By

from libs import config
from utils.mongodbutils import connect_to_db, findone

log = logging.getLogger(__name__)

class StbConfigPage:

    def __init__(self, edriver):
        self.driver = edriver

    __stb_names= (By.XPATH, "//td[contains(text(),'stb_config_name')]//following::td[1]")
    __stbConfigName=(By.ID,"stbConfigName")
    __modAppIp=(By.ID,"modAppIp")
    __passThruIp=(By.ID,"passThruIp")
    __sessionGateWayIp=(By.ID,"sessionGateWayIp")
    __srmIp=(By.ID,"srmIp")
    __srmPort=(By.NAME,"srmPort")
    __lscCommProxyIp=(By.ID,"lscCommProxyIp")
    __interactiveCatalogServerIp=(By.ID,"interactiveCatalogServerIp")
    __serviceGatewayName=(By.NAME,"serviceGatewayName")

    # __save_button=(By.VALUE, "//input[@value='Save']")
    __save_button=(By.XPATH,"//input[@value='Save']")
    __error=(By.XPATH,"//div[@class='error']")
    __delete_stb_config=(By.XPATH,"//td[contains(text(),'stbc_ex3')]//following::input[@class='delete']")
    __stb_names = (By.XPATH, "//td[contains(text(),'stb_config_name')]//following::td[1]")

    stbConfigName = config.get_default("stbConfigName")
    modAppIp = config.get_default("modAppIp")
    passThruIp = config.get_default("passThruIp")
    sessionGateWayIp = config.get_default("sessionGateWayIp")
    srmIp = config.get_default("srmIp")
    srmPort = config.get_default("srmPort")
    lscCommProxyIp = config.get_default("lscCommProxyIp")
    interactiveCatalogServerIp = config.get_default("interactiveCatalogServerIp")
    serviceGatewayName = config.get_default("serviceGatewayName")

    def save_stb_config(self):
        self.driver.find_element(*StbConfigPage.__save_button).click()

    def get_stb_configuration_list(self):
        driver = self.driver
        stb_list=[]
        stb_list.clear()
        # driver.find_element_by_xpath("//td[@id='tvgcmStbConfigMainMenu']").click()
        # driver.find_element_by_xpath("//a[contains(text(),'List STB Configs')]").click()
        stb_names = driver.find_elements(*StbConfigPage.__stb_names)
        for stb in stb_names:
            stb_list.append(stb.text)
        str_stb_list = ', '.join(stb_list)
        log.info("List of available STB Configurations: "+ str_stb_list)
        # return str_stb_list

    def add_stb_config(self):

        driver=self.driver
        driver.find_element(*StbConfigPage.__stbConfigName).send_keys(self.stbConfigName)
        driver.find_element(*StbConfigPage.__modAppIp).send_keys(self.modAppIp)
        driver.find_element(*StbConfigPage.__passThruIp).send_keys(self.passThruIp)
        driver.find_element(*StbConfigPage.__sessionGateWayIp).send_keys(self.sessionGateWayIp)
        driver.find_element(*StbConfigPage.__srmIp).send_keys(self.srmIp)
        driver.find_element(*StbConfigPage.__srmPort).send_keys(self.srmPort)
        driver.find_element(*StbConfigPage.__lscCommProxyIp).clear()
        driver.find_element(*StbConfigPage.__lscCommProxyIp).send_keys(self.lscCommProxyIp)
        driver.find_element(*StbConfigPage.__interactiveCatalogServerIp).send_keys(self.interactiveCatalogServerIp)
        driver.find_element(*StbConfigPage.__serviceGatewayName).send_keys(self.serviceGatewayName)
        self.save_stb_config()
        try:
            assert driver.title == "TVGCM: STB Configs"
            log.info("New stb configuration " + self.stbConfigName + " added !!")
        except AssertionError:
            log.info("Assertion failed. Couldn't Add stb configuration " + self.stbConfigName)

    def verify_error_on_adding_duplicate_stbConfig(self):
        error=self.driver.find_element(*StbConfigPage.__error).is_displayed()
        assert error==True
        log.info(self.driver.find_element(*StbConfigPage.__error).text)

    def delete_stb_config(self):
        time.sleep(2)
        delete_stb=self.driver.find_element(*StbConfigPage.__delete_stb_config)
        self.driver.execute_script("arguments[0].scrollIntoView();", delete_stb)
        delete_stb.click()
        log.info("STB Configuration " + self.stbConfigName + " deleted successfully!!")

    def verify_add_db_stb_config(self):
        DBSERVER = config.get_default("DBSERVER")
        db = connect_to_db(DBSERVER, dbuser='admin', dbpassword='admin1234', dbname='ADAPTERDB')
        read_query = {"stbConfigName": self.stbConfigName}
        query_resp = findone(db, "barker_stb_config", read_query)
        assert query_resp['stbConfigName'] == self.stbConfigName
        log.info("STB Config " + self.stbConfigName + " added to database")

    def verify_delete_db_stb_config(self):
        DBSERVER = config.get_default("DBSERVER")
        db = connect_to_db(DBSERVER, dbuser='admin', dbpassword='admin1234', dbname='ADAPTERDB')
        read_query = {"stbConfigName": self.stbConfigName}
        query_resp = findone(db, "barker_stb_config", read_query)
        # assert query_resp['stbConfigName'] != self.stbConfigName
        if not query_resp:
            log.info("STB Config " + self.stbConfigName + " deleted from database")