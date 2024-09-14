import allure

from pages.login_page import LoginPage


@allure.step("Login to the system")
def do_login(driver, user_name, password):
    login_page = LoginPage(driver)
    login_page.enter_user_name(user_name)
    login_page.enter_password(password)
    login_page.submit_login()