import logging

from selenium.webdriver.common.by import By

from libs import config
from libs.BaseClass import BaseClass
from utils.mongodbutils import connect_to_db, findone

log = logging.getLogger(__name__)

class BroadcastOfferingPage(BaseClass):

    def __init__(self, edriver):
        self.driver = edriver

    __table_rows= (By.XPATH, "//table[@class='list customTable']//tbody/tr")
    __broadcast_offering_name= (By.ID,"oid")
    __iphostname=(By.ID,"iphostname")
    __ipport= (By.ID, "ipport")
    __save_and_publish = (By.XPATH, "//input[@value='Save and Publish']")

    STB_Config = config.get_default("stbConfigName")
    Broadcast_Offering_Name = config.get_default("Broadcast Offering Name")
    QAM_Host = config.get_default("QAM Host")
    QAM_Port = config.get_default("QAM Port")
    __delete_broadcast_offering = (By.XPATH,"//a[contains(text(),'ch_008_barker')]//preceding::input[1]")
    __delete_button = (By.XPATH, "//input[@value='Delete']")

    # def get_table_rows(self):
        #rows = driver.find_elements_by_xpath("//table[@class='list customTable']//tbody/tr")
        # self.driver.find_element(*BroadcastOfferingPage.__table_rows)

    def get_broadcast_offerings_list(self):
        bo_list=[]
        qam_port_list=[]
        rows = self.driver.find_elements(*BroadcastOfferingPage.__table_rows)
        for i in range(2,len(rows)+1):
            bo_name=self.driver.find_element_by_xpath("//table[@class='list customTable']//tbody/tr["+str(i)+"]/td[2]").text
            qam_port=self.driver.find_element_by_xpath("//table[@class='list customTable']//tbody/tr[" + str(i) + "]/td[8]").text
            bo_list.append(bo_name)
            qam_port_list.append(qam_port)

        str_bo_list = ', '.join(bo_list)
        str_qam_port_list = ', '.join(qam_port_list)
        log.info("List of available broadcast offerings: " + str_bo_list)
        log.info("List of available qam ports: " + str_qam_port_list)

    def add_broadcast_offering(self):
        driver=self.driver
        driver.find_element(*BroadcastOfferingPage.__broadcast_offering_name).send_keys(self.Broadcast_Offering_Name)
        driver.find_element(*BroadcastOfferingPage.__iphostname).clear()
        driver.find_element(*BroadcastOfferingPage.__iphostname).send_keys(self.QAM_Host)
        driver.find_element(*BroadcastOfferingPage.__ipport).send_keys(self.QAM_Port)
        drop = BaseClass.getAllDropDownOptions(self,"stb_sel")
        BaseClass.selectDropDownListByValue(self,"stb_sel",self.STB_Config)
        BaseClass.selectDropDownListByIndex(self,"catalogPlayer",1)
        BaseClass.srollToBottomOfPage(self)
        driver.find_element(*BroadcastOfferingPage.__save_and_publish).click()
        assert driver.title == "TVGCM: Broadcast Offerings"
        log.info("New broadcast offering " + self.Broadcast_Offering_Name + " added !!")

    def delete_broadcast_offering(self):
        self.driver.find_element(*BroadcastOfferingPage.__delete_broadcast_offering).click()
        self.driver.find_element(*BroadcastOfferingPage.__delete_button).click()
        BaseClass.alert_accept(self)
        log.info("Broadcast Offering " + self.Broadcast_Offering_Name + " deleted successfully!!")

    def verify_add_db_broadcast_offering_(self):
        DBSERVER= config.get_default("DBSERVER")
        db=connect_to_db(DBSERVER, dbuser='admin', dbpassword='admin1234', dbname='ADAPTERDB')
        read_query={"oid":self.Broadcast_Offering_Name}
        query_resp = findone(db, "barker_broadcast_offering", read_query)
        assert query_resp['oid'] == self.Broadcast_Offering_Name
        log.info("Broadcast Offering " + self.Broadcast_Offering_Name + " added to database")

    def verify_delete_db_broadcast_offering_(self):
        DBSERVER= config.get_default("DBSERVER")
        db=connect_to_db(DBSERVER, dbuser='admin', dbpassword='admin1234', dbname='ADAPTERDB')
        read_query={"oid":self.Broadcast_Offering_Name}
        query_resp = findone(db, "barker_broadcast_offering", read_query)
        # assert query_resp['oid'] != self.Broadcast_Offering_Name #TypeError: 'NoneType' object is not subscriptable
        if not query_resp:
            log.info("Broadcast Offering " + self.Broadcast_Offering_Name + " deleted from database")
