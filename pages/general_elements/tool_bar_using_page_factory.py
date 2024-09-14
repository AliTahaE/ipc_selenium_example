import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Toolbar2:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Define an explicit wait

    # Locators
    page_heading_locator = (By.CSS_SELECTOR, "h6.oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module")
    user_management_heading_locator = (By.XPATH, "//h6[text()='User Management']")
    upgrade_button_locator = (By.XPATH, "//button[text()=' Upgrade']")
    profile_image_locator = (By.XPATH, "//li[@data-v-bdd6d943]//img")
    profile_name_locator = (By.XPATH, "//li[@data-v-bdd6d943]//p")
    dynamic_tool_bar_elements_locator = (By.XPATH, "//nav//ul//li[@class='oxd-topbar-body-nav-tab']")

    # Methods to interact with the elements
    @allure.step("Get page header text")
    def get_page_header(self):
        return self.driver.find_element(*self.page_heading_locator).text

    @allure.step("Get User Management header text")
    def get_user_management_header(self):
        return self.driver.find_element(*self.user_management_heading_locator).text

    @allure.step("Click on the upgrade button")
    def click_upgrade_button(self):
        self.driver.find_element(*self.upgrade_button_locator).click()

    @allure.step("Click on the profile image")
    def click_profile_image(self):
        self.driver.find_element(*self.profile_image_locator).click()

    @allure.step("Get profile name text")
    def get_profile_name(self):
        return self.driver.find_element(*self.profile_name_locator).text

    @allure.step("Get all dynamic toolbar items")
    def get_dynamic_items(self):
        return self.wait.until(EC.presence_of_all_elements_located(self.dynamic_tool_bar_elements_locator))

    @allure.step("Check if item with expected text is visible")
    def is_item_visible(self, expected_text):
        dynamic_items = self.get_dynamic_items()
        dynamic_items_text = [item.text for item in dynamic_items]
        return expected_text in dynamic_items_text
