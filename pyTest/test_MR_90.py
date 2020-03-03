import pytest
import logging

from PageObject.HomePage import HomePage
from libs.BaseClass import BaseClass
from resources.CatalogPageData import CatalogPageData

log = logging.getLogger(__name__)

class Test_MR_90(BaseClass):

    def test_add_new_hotLaunchSourceID(self, get_hotLaunchSourceId):
        #add a new category
        HOME_PAGE=HomePage(self.driver)
        log.info("Login and goto Homepage")
        CATALOG_PAGE=HOME_PAGE.goto_add_category()
        log.info("Goto Add Category")
        CATALOG_PAGE.add_and_publish_category(get_hotLaunchSourceId["hlsId"])
        log.info("Add a new category and publish it")
        #delete category
        HOME_PAGE.goto_list_categories()
        CATALOG_PAGE.delete_category(get_hotLaunchSourceId["hlsId"])

    def test_add_duplicate_hotLaunchSourceId(self, get_dup_hotLaunchSourceId):
        # add a new category
        HOME_PAGE = HomePage(self.driver)
        CATALOG_PAGE = HOME_PAGE.goto_add_category()
        CATALOG_PAGE.add_and_publish_category(get_dup_hotLaunchSourceId["hlsId"])
        log.info("Add and publish a new category")

        # add a new category with duplicate hotLaunchSourceId
        CATALOG_PAGE = HOME_PAGE.goto_add_category()
        CATALOG_PAGE.add_and_publish_category(get_dup_hotLaunchSourceId["hlsId"])
        log.info("Add a new category with duplicate hotLaunchSourceId")

        # delete category
        HOME_PAGE.goto_list_categories()
        CATALOG_PAGE.delete_category(get_dup_hotLaunchSourceId["hlsId"])

    def test_get_list(self):
        HOME_PAGE = HomePage(self.driver)
        CATALOG_PAGE = HOME_PAGE.goto_add_category()
        HOME_PAGE.goto_list_categories()
        CATALOG_PAGE.list_hotLaunchSource_Ids()
        # hls=CATALOG_PAGE.list_hotLaunchSource_Ids()
        # log.info("List of available categories: "+hls)

    @pytest.fixture(params=CatalogPageData.test_catalogPage_data)
    def get_hotLaunchSourceId(self, request):
        return request.param

    @pytest.fixture(params=CatalogPageData.test_catalogPage_data_1)
    def get_dup_hotLaunchSourceId(self,request):
        return request.param
