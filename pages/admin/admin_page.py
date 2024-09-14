import allure
from selenium.webdriver.common.by import By

from pages.basicPage.basic_page import BasicPage


class AdminPage(BasicPage):

    def __init__(self, driver):
        super().__init__(driver)

    add_user = (By.XPATH,  "//button[text()=' Add ']")


    @allure.step("Click add user")
    def click_add_user(self):
        self.driver.find_element(*self.add_user).click()