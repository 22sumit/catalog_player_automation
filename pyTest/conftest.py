import time
import pytest
from selenium import webdriver
from PageObject.LoginPage import LoginPage
from utils import reportutils
driver=None

@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = webdriver.Chrome(executable_path='../webdrivers/chromedriver.exe')
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    LOGIN_PAGE = LoginPage(driver)
    LOGIN_PAGE.login()
    LOGIN_PAGE.assert_title()

    yield
    # reportutils.test_report()
    time.sleep(1)
    LOGIN_PAGE.logout()
    driver.quit()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)

