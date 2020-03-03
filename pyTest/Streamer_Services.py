import pytest
import utils.sshutils as sshutils
import libs.config as config
from pyTest import conftest as codebase
import pyTest.Catalog_Player_Status as CPS

class Test_Streamer_Service():

    @pytest.fixture(scope="module")
    def test_setup(self):
        codebase.test_login()
        yield
        codebase.test_logout()
        print("test completed")

    # @pytest.mark.skip(reason='skipping test_get_cp_ip_address currently')
    def test_primary_off_standby_on(self, test_setup):
        primary_ip_with_port = CPS.Test_CP_Status.test_get_primary_ip(self, test_setup)
        primary_ip = primary_ip_with_port[:-5:1]
        print("primary_ip: ", primary_ip)
        ip = config.get_default("ssh_ip")
        username = config.get_default("ssh_username")
        password = config.get_default("ssh_password")
        sshutils.ssh_connect(ip,username,password)
        sshutils.ssh_stop_service(primary_ip)

        primary_status, standby_status = CPS.Test_CP_Status.test_get_cp_status(self, test_setup)
        assert primary_status=='Down'
        assert standby_status=='Up'
        sshutils.ssh_start_service()
        sshutils.ssh_close(ip,primary_ip)

    def test_primary_on_standby_off(self, test_setup):
        standby_ip_with_port = CPS.Test_CP_Status.test_get_standby_ip(self, test_setup)
        standby_ip=standby_ip_with_port[:-5:1]
        print("standby_ip: ", standby_ip)
        ip = config.get_default("ssh_ip")
        username = config.get_default("ssh_username")
        password = config.get_default("ssh_password")
        sshutils.ssh_connect(ip,username,password)
        sshutils.ssh_stop_service(standby_ip)

        primary_status, standby_status = CPS.Test_CP_Status.test_get_cp_status(self, test_setup)
        assert primary_status=='Up'
        assert standby_status=='Down'
        sshutils.ssh_start_service()
        sshutils.ssh_close(ip,standby_ip)

    def test_primary_off_standby_off(self, test_setup):
        primary_ip_with_port = CPS.Test_CP_Status.test_get_primary_ip(self, test_setup)
        primary_ip = primary_ip_with_port[:-5:1]
        print("primary_ip: ", primary_ip)
        standby_ip_with_port = CPS.Test_CP_Status.test_get_standby_ip(self, test_setup)
        standby_ip = standby_ip_with_port[:-5:1]
        print("standby_ip: ", standby_ip)
        ip = config.get_default("ssh_ip")
        username = config.get_default("ssh_username")
        password = config.get_default("ssh_password")
        sshutils.ssh_connect(ip,username,password)
        sshutils.ssh_stop_service(primary_ip)
        sshutils.ssh_stop_service(standby_ip)

        primary_status, standby_status = CPS.Test_CP_Status.test_get_cp_status(self, test_setup)
        assert primary_status=='Down'
        assert standby_status=='Down'
        sshutils.ssh_start_service()
        sshutils.ssh_close(ip,standby_ip)