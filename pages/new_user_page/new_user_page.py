import allure
from selenium.webdriver.common.by import By
from pages.basicPage.basic_page import BasicPage

class NewUserPage(BasicPage):

    def __init__(self, driver):
        super().__init__(driver)

    # Locator definitions with By.<type>
    locators = {
        'add_user_heading': (By.XPATH, "//h6[text()='Add User']"),
        'employee_name': (By.XPATH, "//input[contains(@placeholder, 'Type for hints')]"),
        'user_name': (By.XPATH, "//div[@data-v-957b4417]/input"),
        'password': (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input"),
        'confirm_password': (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input"),
        'user_role_dropdown': (By.CSS_SELECTOR, ".oxd-select-text.oxd-select-text--active"),
        'status_dropdown': (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div"),
        'save_button': (By.XPATH, "//button[text()=' Save ']"),
        'user_employees_list': (By.XPATH, "//div[@role='listbox']")
    }

    @allure.step("Select employee by name from the list")
    def select_employee(self, searchregex, employee_name):
        # Locate the employee input field and set text
        employee_input = self.driver.find_element(*self.locators['employee_name'])
        employee_input.send_keys(searchregex)

        # Locate the specific employee from the list based on the employee name
        employee_element = (By.XPATH, f"//div//span[text()='{employee_name}']")
        self.driver.find_element(*employee_element).click()

    @allure.step("Type user name into the user name field")
    def type_user_name(self, name):
        user_input = self.driver.find_element(*self.locators['user_name'])
        user_input.send_keys(name)

    @allure.step("Type password into the password field")
    def type_password(self, password_value):
        password_input = self.driver.find_element(*self.locators['password'])
        password_input.send_keys(password_value)

    @allure.step("Type confirm password into the confirm password field")
    def type_confirm_password(self, password_value):
        confirm_password_input = self.driver.find_element(*self.locators['confirm_password'])
        confirm_password_input.send_keys(password_value)

    @allure.step("Select user role from the dropdown")
    def select_user_role(self, role):
        role_dropdown = self.driver.find_element(*self.locators['user_role_dropdown'])
        role_dropdown.click()

        role_option = (By.XPATH, f"//div//span[text()='{role}']")
        self.driver.find_element(*role_option).click()

    @allure.step("Select status from the status dropdown")
    def select_status(self, status):
        status_dropdown = self.driver.find_element(*self.locators['status_dropdown'])
        status_dropdown.click()

        status_option = (By.XPATH, f"//div//span[text()='{status}']")
        self.driver.find_element(*status_option).click()

    @allure.step("Click on the save button")
    def click_save(self):
        save_button = self.driver.find_element(*self.locators['save_button'])
        save_button.click()

    @allure.step("Get text of the employees list")
    def get_employees(self):
        return self.driver.find_element(*self.locators['user_employees_list']).text
