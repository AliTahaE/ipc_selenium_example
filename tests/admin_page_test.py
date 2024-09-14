import time

import allure
import pytest

from pages.admin.admin_page import AdminPage
from pages.dashboard.dashboard_page import DashboardPage
from pages.new_user_page.new_user_page import NewUserPage
from utils import driver_wrapper, test_utils
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
            allure.attach(driver.get_screenshot_as_png(), name="screenshot.png", attachment_type=allure.attachment_type.PNG)


def test_add_new_user(driver):


    login_utils.do_login(driver,'Admin', 'admin123')

    dashboard_page = DashboardPage(driver)

    dashboard_page.navigate_to_admin()

    admin_page = AdminPage(driver)

    admin_page.click_add_user()

    new_user_page = NewUserPage(driver)

    new_user_page.type_user_name('Ali Taha'.join(test_utils.generate_random_string(4)))

    new_user_page.select_employee('AL', 'ftioiu  ltpugr')
    time.sleep(3)

    new_user_page.select_user_role('ESS')
    new_user_page.select_status('Enabled')

    new_user_page.type_password('1234567a')
    new_user_page.type_confirm_password('1234567a')

    new_user_page.click_save()
    time.sleep(5)