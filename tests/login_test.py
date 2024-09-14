import time

import allure
import pytest

from pages.general_elements.side_panel import SidePanel
from pages.general_elements.tool_bar import Toolbar
from pages.general_elements.tool_bar_using_page_factory import Toolbar2
from utils import driver_wrapper
from utils.pagesUtils import login_utils


@pytest.fixture(scope="session")
def browser_name():
    return "edge"

@pytest.fixture(scope="session")
def url():
    return "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

@pytest.fixture
def driver(browser_name, url):
    driver = driver_wrapper.init_browser(browser_name, url)
    yield driver
    driver_wrapper.quit_driver(driver)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and (report.failed or report.outcome == "broken"):
        driver = item.funcargs.get('driver')
        if driver:
            allure.attach(driver.get_screenshot_as_png(), name="screenshot12.png", attachment_type=allure.attachment_type.PNG)


@allure.title("Test login functionality")
def test_login(driver):

    login_utils.do_login(driver, 'Admin', 'admin123')

    toolbar = Toolbar(driver)
    sidePanel = SidePanel(driver)
    toolbar_2 = Toolbar2(driver)


    sidePanel.navigate_to_admin()
    assert 'Admin' == toolbar.get_page_header()
    assert 'User Management' == toolbar.get_user_management_header().text
    time.sleep(5)


    toolbar_2.click_upgrade_button()
    time.sleep(5)

    sidePanel.navigate_to_pim()
    assert 'PIM' == toolbar.get_page_header()
    time.sleep(5)


    sidePanel.navigate_to_leave()
    assert 'Leave' == toolbar.get_page_header()
    time.sleep(5)


    sidePanel.navigate_to_time()
    assert 'Time' == toolbar.get_page_header()
    time.sleep(5)


    sidePanel.navigate_to_recruitment()
    assert 'Recruitment' == toolbar.get_page_header()
    time.sleep(5)


    sidePanel.navigate_to_my_info()
    assert 'My Info' == toolbar.get_page_header()
    time.sleep(5)


    sidePanel.navigate_to_performance()
    assert 'Performance' == toolbar.get_page_header()
    time.sleep(5)


    sidePanel.navigate_to_dashboard()
    assert 'Dashboard' == toolbar.get_page_header()
    time.sleep(5)


    sidePanel.navigate_to_directory()
    assert 'Directory' == toolbar.get_page_header()
    time.sleep(5)


    sidePanel.navigate_to_maintenance()
    time.sleep(5)
    driver.back()


    sidePanel.navigate_to_claim()
    assert 'Claim' == toolbar.get_page_header()
    time.sleep(5)


    sidePanel.navigate_to_buzz()
    assert 'Buzz' == toolbar.get_page_header()
    time.sleep(5)



