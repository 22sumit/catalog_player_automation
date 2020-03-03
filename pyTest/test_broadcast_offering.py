from PageObject.HomePage import HomePage
from libs.BaseClass import BaseClass
# import allure

class Test_Broadcast_Offering(BaseClass):

    # @allure.step('List of all available Broadcast Offerings')
    # @pytest.mark.skip(reason='skipping bo listing currently')
    def test_get_broadcast_offering_list(self):
        driver = self.driver
        HOME_PAGE=HomePage(driver)
        BROADCAST_OFFERING_LIST_PAGE = HOME_PAGE.goto_list_broadcast_offering_page()
        BROADCAST_OFFERING_LIST_PAGE.get_broadcast_offerings_list()

    # # @allure.step('Add a new Broadcast Offering')
    def test_add_broadcast_offering(self):
        #add new broadcast offering
        HOME_PAGE = HomePage(self.driver)
        STB_CONFIG_PAGE = HOME_PAGE.goto_add_stbConfig_page()
        STB_CONFIG_PAGE.add_stb_config()
        BROADCAST_OFFERING_ADD_PAGE = HOME_PAGE.goto_add_broadcast_offering_page()
        BROADCAST_OFFERING_ADD_PAGE.add_broadcast_offering()
        BROADCAST_OFFERING_ADD_PAGE.verify_add_db_broadcast_offering_()

        #delete broadcast offering
        BROADCAST_OFFERING_ADD_PAGE.delete_broadcast_offering()
        BROADCAST_OFFERING_ADD_PAGE.verify_delete_db_broadcast_offering_()
        # delete stb config
        HOME_PAGE.goto_list_stbConfig_page()
        STB_CONFIG_PAGE.delete_stb_config()
