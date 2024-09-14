import allure
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    user_name_locator = (By.NAME, "username")
    password_locator = (By.NAME, "password")
    login_button_locator = (By.CSS_SELECTOR, ".oxd-button")

    # Methods to interact with elements
    @allure.step("Enter username into the username field")
    def enter_user_name(self, username):
        user_name_element = self.driver.find_element(*self.user_name_locator)
        user_name_element.clear()
        user_name_element.send_keys(username)

    @allure.step("Enter password into the password field")
    def enter_password(self, password):
        password_element = self.driver.find_element(*self.password_locator)
        password_element.clear()
        password_element.send_keys(password)

    @allure.step("Click on the login button")
    def submit_login(self):
        login_button_element = self.driver.find_element(*self.login_button_locator)
        login_button_element.click()
