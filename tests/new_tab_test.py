import time

import allure
import pytest

from pages.general_elements.side_panel import SidePanel
from pages.general_elements.tool_bar import Toolbar
from pages.upgrade_page import UpgradePage
from utils import driver_wrapper, browser_tabs_utils
from utils.pagesUtils import login_utils

@pytest.fixture(scope="session")
def browser_name():
    return "edge"

@pytest.fixture(scope="session")
def url():
    return "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

@pytest.fixture(scope="function")
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
            allure.attach(driver.get_screenshot_as_png(), name="screenshot45.png", attachment_type=allure.attachment_type.PNG)



@allure.title("test new browser tabs functionality")
def test_new_tab(driver):

    login_utils.do_login(driver, 'Admin', "admin123")
    time.sleep(5)
    toolbar = Toolbar(driver)
    toolbar.click_upgrade_button()

    default_window_handler = driver.current_window_handle
    browser_tabs_utils.switch_to_new_tab(driver, default_window_handler, driver.window_handles)


    upgrade_page = UpgradePage(driver)
    upgrade_page.click_book_a_demo()

    time.sleep(5)
    upgrade_page.type_full_name("Ali Taha")
    upgrade_page.type_phone_number('545646')
    upgrade_page.type_email('a@b.c')
    upgrade_page.type_company("alitechs")
    upgrade_page.submit()

    driver_wrapper.close_current_window(driver)

    browser_tabs_utils.switch_to_default_screen(driver, default_window_handler)

    side_panel = SidePanel(driver)

    side_panel.navigate_to_buzz()

