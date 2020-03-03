import pytest
import allure
import time
import libs.config as config
from pyTest import conftest as codebase
import libs.Function_Library as flib

class Test_CP_Status():

    @pytest.fixture(scope="module")
    def test_setup(self):
        codebase.test_login()
        yield
        codebase.test_logout()
        print("test completed")

    @allure.step('Get Primary IP')
    def test_get_primary_ip(self, test_setup):
        codebase.driver.find_element_by_xpath("//td[@id='tvgcmHomeMainMenu']").click()
        primary_ip_port = config.get_default("primary")
        primary = flib.get_text("//span[contains(text(),'Duluth_Primary_Service')]//following::td[2]")
        print("primary: ", primary)
        assert primary == primary_ip_port, "Primary IP mismatch !!"
        return primary

    @allure.step('Get Standby IP')
    def test_get_standby_ip(self, test_setup):
        codebase.driver.find_element_by_xpath("//td[@id='tvgcmHomeMainMenu']").click()
        standby_ip_port = config.get_default("standby")
        standby = flib.get_text("//span[contains(text(),'Duluth_Standby_Service')]//following::td[2]")
        print("standby: ", standby)
        assert standby == standby_ip_port, "Standby IP mismatch !!"
        return standby

    @allure.step('Get Catalog Player Status')
    def test_get_cp_status(self,test_setup):
        time.sleep(5)
        codebase.driver.refresh()
        time.sleep(5)
        primary_status= codebase.driver.find_element_by_xpath("//span[contains(text(),'Duluth_Primary_Service')]//following::img[1]").get_attribute("title")
        print("Primary Catalog Player Status: ",primary_status)
        standby_status= codebase.driver.find_element_by_xpath("//span[contains(text(),'Duluth_Standby_Service')]//following::img[1]").get_attribute("title")
        print("Standby Catalog Player Status: ",standby_status)
        return primary_status, standby_status