import inspect
import time

import pytest
import logging
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

log = logging.getLogger(__name__)

@pytest.mark.usefixtures("setup")
class BaseClass():

    __stb_config_missing = (By.XPATH, "//li[contains(text(),'STB Config is required to save the broadcast offer')]")

    def selectDropDownListByValue(self,DropDownList_property,DropDownList_Val):
        dropDownList = Select(self.driver.find_element_by_id(DropDownList_property))
        try:
            dropDownList.select_by_value(DropDownList_Val)
        except NoSuchElementException:
            if DropDownList_property == "stb_sel":
                log.info("Required STB Config is missing. Couldn't add broadcast offering.")
                log.error("STB Config is required to save the broadcast offering.")

    def selectDropDownListByIndex(self,DropDownList_property,DropDownList_Val):
        dropDownList = Select(self.driver.find_element_by_name(DropDownList_property))
        dropDownList.select_by_index(DropDownList_Val)

    def getAllDropDownOptions(self,DropDownList_property):
        drop=[]
        dropDownList = Select(self.driver.find_element_by_id(DropDownList_property))
        for option in dropDownList.options:
            drop.append(option.text)
        return drop

    def srollToBottomOfPage(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def alert_accept(self):
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present(),
                                                    'Timed out waiting for confirmation popup to appear.')
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            print("no alert present")

    def getWebTableRowCount(self, WebTable_Element):
        rows = WebTable_Element.find_elements_by_xpath(".//tbody[1]//tr")
        return len(rows)

    def getWebTableColumnCount(self, WebTable_Element):
        cols=WebTable_Element.find_elements_by_xpath(".//tbody[1]/tr[1]/td")
        return len(cols)