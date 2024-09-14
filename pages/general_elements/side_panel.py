import allure
from selenium.webdriver.common.by import By

class SidePanel:
    def __init__(self, driver):
        self.driver = driver

    # Locators as class properties
    search_input_locator = (By.CSS_SELECTOR, ".oxd-main-menu-search input")
    admin_link_locator = (By.XPATH, "//a[contains(@href, 'viewAdminModule')]")
    pim_link_locator = (By.XPATH, "//a[contains(@href, 'viewPimModule')]")
    leave_link_locator = (By.XPATH, "//a[contains(@href, 'viewLeaveModule')]")
    time_link_locator = (By.XPATH, "//a[contains(@href, 'viewTimeModule')]")
    recruitment_link_locator = (By.XPATH, "//a[contains(@href, 'viewRecruitmentModule')]")
    my_info_link_locator = (By.XPATH, "//a[contains(@href, 'viewMyDetails')]")
    performance_link_locator = (By.XPATH, "//a[contains(@href, 'viewPerformanceModule')]")
    dashboard_link_locator = (By.XPATH, "//a[contains(@href, 'dashboard')]")
    directory_link_locator = (By.XPATH, "//a[contains(@href, 'viewDirectory')]")
    maintenance_link_locator = (By.XPATH, "//a[contains(@href, 'viewMaintenanceModule')]")
    claim_link_locator = (By.XPATH, "//a[contains(@href, 'viewClaimModule')]")
    buzz_link_locator = (By.XPATH, "//a[contains(@href, 'viewBuzz')]")

    # Methods to interact with the elements
    @allure.step("Enter search text into the search input field")
    def enter_search_text(self, text):
        search_input = self.driver.find_element(*self.search_input_locator)
        search_input.clear()
        search_input.send_keys(text)

    @allure.step("Navigate to the Admin module")
    def navigate_to_admin(self):
        self.driver.find_element(*self.admin_link_locator).click()

    @allure.step("Navigate to the PIM module")
    def navigate_to_pim(self):
        self.driver.find_element(*self.pim_link_locator).click()

    @allure.step("Navigate to the Leave module")
    def navigate_to_leave(self):
        self.driver.find_element(*self.leave_link_locator).click()

    @allure.step("Navigate to the Time module")
    def navigate_to_time(self):
        self.driver.find_element(*self.time_link_locator).click()

    @allure.step("Navigate to the Recruitment module")
    def navigate_to_recruitment(self):
        self.driver.find_element(*self.recruitment_link_locator).click()

    @allure.step("Navigate to My Info section")
    def navigate_to_my_info(self):
        self.driver.find_element(*self.my_info_link_locator).click()

    @allure.step("Navigate to the Performance module")
    def navigate_to_performance(self):
        self.driver.find_element(*self.performance_link_locator).click()

    @allure.step("Navigate to the Dashboard")
    def navigate_to_dashboard(self):
        self.driver.find_element(*self.dashboard_link_locator).click()

    @allure.step("Navigate to the Directory")
    def navigate_to_directory(self):
        self.driver.find_element(*self.directory_link_locator).click()

    @allure.step("Navigate to the Maintenance module")
    def navigate_to_maintenance(self):
        self.driver.find_element(*self.maintenance_link_locator).click()

    @allure.step("Navigate to the Claim module")
    def navigate_to_claim(self):
        self.driver.find_element(*self.claim_link_locator).click()

    @allure.step("Navigate to the Buzz section")
    def navigate_to_buzz(self):
        self.driver.find_element(*self.buzz_link_locator).click()
