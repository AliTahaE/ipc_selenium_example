import allure
from selenium.webdriver.common.by import By

class UpgradePage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    book_a_demo_locator = (By.XPATH, "//a[contains(@href, 'demo-submit')]")
    full_name_text_field_locator = (By.ID, 'Form_getForm_Name')
    phone_number_text_field_locator = (By.ID, 'Form_getForm_Contact')
    email_text_field_locator = (By.ID, 'Form_getForm_Email')
    company_text_field_locator = (By.ID, 'Form_getForm_CompanyName')
    country_dropdown_locator = (By.ID, 'Form_getForm_Country_Holder')
    submit_button_locator = (By.ID, 'Form_getForm_action_submitForm')

    # Methods to interact with elements
    @allure.step("Click on 'Book a Demo' link")
    def click_book_a_demo(self):
        self.driver.find_element(*self.book_a_demo_locator).click()

    @allure.step("Type full name into the text field")
    def type_full_name(self, text):
        full_name_field = self.driver.find_element(*self.full_name_text_field_locator)
        full_name_field.clear()
        full_name_field.send_keys(text)

    @allure.step("Type phone number into the text field")
    def type_phone_number(self, text):
        phone_number_field = self.driver.find_element(*self.phone_number_text_field_locator)
        phone_number_field.clear()
        phone_number_field.send_keys(text)

    @allure.step("Type email into the text field")
    def type_email(self, text):
        email_field = self.driver.find_element(*self.email_text_field_locator)
        email_field.clear()
        email_field.send_keys(text)

    @allure.step("Type company name into the text field")
    def type_company(self, text):
        company_field = self.driver.find_element(*self.company_text_field_locator)
        company_field.clear()
        company_field.send_keys(text)

    @allure.step("Submit the form")
    def submit(self):
        self.driver.find_element(*self.submit_button_locator).click()
