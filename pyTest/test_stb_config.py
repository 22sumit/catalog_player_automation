import logging
from PageObject.HomePage import HomePage
from libs.BaseClass import BaseClass
import allure

log = logging.getLogger(__name__)
# stb_list=""
class Test_STB_Config(BaseClass):

    def test_get_stb_configuration_list(self):
        # global stb_list
        HOME_PAGE = HomePage(self.driver)
        STB_CONFIG_LIST_PAGE = HOME_PAGE.goto_list_stbConfig_page()
        STB_CONFIG_LIST_PAGE.get_stb_configuration_list()

    # @allure.step('Add a new STB Configuration')
    def test_stb_config_add(self):

        # add stb config
        HOME_PAGE= HomePage(self.driver)
        STB_CONFIG_ADD_PAGE = HOME_PAGE.goto_add_stbConfig_page()
        STB_CONFIG_ADD_PAGE.add_stb_config()
        STB_CONFIG_ADD_PAGE.get_stb_configuration_list()
        STB_CONFIG_ADD_PAGE.verify_add_db_stb_config()

        # delete stb config
        STB_CONFIG_LIST_PAGE=HOME_PAGE.goto_list_stbConfig_page()
        STB_CONFIG_LIST_PAGE.delete_stb_config()
        STB_CONFIG_LIST_PAGE.verify_delete_db_stb_config()
        STB_CONFIG_LIST_PAGE.get_stb_configuration_list()

    # @allure.step('Add duplicate STB Configuration')
    def test_dup_stb_config_add(self):
        #add first stb config
        HOME_PAGE = HomePage(self.driver)
        STB_CONFIG_ADD_PAGE = HOME_PAGE.goto_add_stbConfig_page()
        STB_CONFIG_ADD_PAGE.add_stb_config()
        HOME_PAGE.goto_add_stbConfig_page()
        STB_CONFIG_ADD_PAGE.verify_add_db_stb_config()

        # add duplicate stb config
        STB_CONFIG_ADD_PAGE = HOME_PAGE.goto_add_stbConfig_page()
        STB_CONFIG_ADD_PAGE.add_stb_config()
        STB_CONFIG_ADD_PAGE.verify_error_on_adding_duplicate_stbConfig()
        STB_CONFIG_LIST_PAGE=HOME_PAGE.goto_list_stbConfig_page()

        #delete stb config
        STB_CONFIG_LIST_PAGE.delete_stb_config()
        STB_CONFIG_LIST_PAGE.verify_delete_db_stb_config()