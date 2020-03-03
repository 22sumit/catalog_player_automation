import allure

from PageObject.HomePage import HomePage
from libs.BaseClass import BaseClass
from utils import reportutils

class Test_complete_flow(BaseClass):

    @allure.step('test stb configuration and broadcast offering flow')
    def test_cp_add(self):

        #add stb configuration
        HOME_PAGE = HomePage(self.driver)
        STB_CONFIG_PAGE = HOME_PAGE.goto_add_stbConfig_page()
        STB_CONFIG_PAGE.add_stb_config()
        STB_CONFIG_PAGE.verify_add_db_stb_config()

        #add broadcast offering
        HOME_PAGE = HomePage(self.driver)
        BROADCAST_OFFERING_PAGE = HOME_PAGE.goto_add_broadcast_offering_page()
        BROADCAST_OFFERING_PAGE.add_broadcast_offering()

        # delete broadcast offering
        BROADCAST_OFFERING_PAGE.delete_broadcast_offering()
        BROADCAST_OFFERING_PAGE.verify_delete_db_broadcast_offering_()

        # delete stb configuration
        HOME_PAGE.goto_list_stbConfig_page()
        STB_CONFIG_PAGE.delete_stb_config()
        STB_CONFIG_PAGE.verify_delete_db_stb_config()
