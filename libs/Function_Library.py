# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import TimeoutException
#
# def selectDropDownListByValue(DropDownList_property,DropDownList_Val, driver):
#     dropDownList = Select(driver.find_element_by_name(DropDownList_property))
#     dropDownList.select_by_value(DropDownList_Val)
#
# def selectDropDownListByIndex(DropDownList_property,DropDownList_Val, driver):
#     dropDownList = Select(driver.find_element_by_name(DropDownList_property))
#     dropDownList.select_by_index(DropDownList_Val)
#
# def getAllDropDownOptions(DropDownList_property, driver):
#     drop=[]
#     dropDownList = Select(driver.find_element_by_name(DropDownList_property))
#     for option in dropDownList.options:
#         drop.append(option.text)
#     return drop
#
# def getWebTableRowCount(WebTable_Element):
#     rows=WebTable_Element.find_elements_by_xpath(".//tbody[1]//tr")
#     return len(rows)
#
# def getWebTableColumnCount(WebTable_Element):
#     cols=WebTable_Element.find_elements_by_xpath(".//tbody[1]/tr[1]/td")
#     return len(cols)
#
# def alert_accept(driver):
#     try:
#         WebDriverWait(driver, 3).until(EC.alert_is_present(),
#                                                 'Timed out waiting for confirmation popup to appear.')
#         alert = driver.switch_to.alert
#         alert.accept()
#     except TimeoutException:
#         print("no alert")
#
# def get_text(xpath_identifier, driver):
#     webElement_text=driver.find_element_by_xpath(xpath_identifier).text
#     return webElement_text
#
# def click_element(element_identifier, driver):
#     driver.find_element_by_xpath(element_identifier).click()

import pytest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from libs.BaseClass import BaseClass



class Function_lib():
    global driver

    def __init__(self,driver):
        self.driver=driver

    def get_text(xpath_identifier):
        webElement_text=driver.find_element_by_xpath(xpath_identifier).text
        return webElement_text
