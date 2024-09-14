import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Toolbar:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    page_heading = (By.CSS_SELECTOR, "h6.oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module")
    user_management_heading = (By.XPATH, "//h6[text()='User Management']")
    upgrade_button = (By.XPATH, "//button[text()=' Upgrade']")
    profile_image = (By.XPATH, "//li[@data-v-bdd6d943]//img")
    profile_name = (By.XPATH, "//li[@data-v-bdd6d943]//p")
    dynamic_tool_bar_elements = (By.XPATH, "//nav//ul//li[@class='oxd-topbar-body-nav-tab']")

    @allure.step("Get page header text")
    def get_page_header(self):
        return self.driver.find_element(*self.page_heading).text

    @allure.step("Get user management header element")
    def get_user_management_header(self):
        return self.driver.find_element(*self.user_management_heading)

    @allure.step("Click on the upgrade button")
    def click_upgrade_button(self):
        self.driver.find_element(*self.upgrade_button).click()

    @allure.step("Click on the profile image")
    def click_profile_image(self):
        self.driver.find_element(*self.profile_image).click()

    @allure.step("Get profile name")
    def get_profile_name(self):
        return self.driver.find_element(*self.profile_name).text

    @allure.step("Get dynamic toolbar items")
    def get_dynamic_items(self):
        return self.wait.until(EC.presence_of_all_elements_located(self.dynamic_tool_bar_elements))

    @allure.step("Check if item with expected text is visible")
    def is_item_visible(self, expected_text):
        dynamic_items = self.get_dynamic_items()
        dynamic_items_text = [item.text for item in dynamic_items]
        return expected_text in dynamic_items_text
