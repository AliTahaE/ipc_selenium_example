import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.options import Options

@allure.step("Browser initialization")
def init_browser(browser_name, url):
    global driver
    if browser_name.lower() == "chrome":
        service = Service('C:\Development\selenium_project\\tests\driver\chromedriver.exe')
        driver = webdriver.Chrome(service=service)
    elif browser_name.lower() == "firefox":
        service = Service('C:\Development\selenium_project\\tests\driver\geckodriver.exe')
        driver = webdriver.Firefox(service=service)
    elif browser_name.lower() == "edge":
        service = Service("C:\Development\selenium_project\\tests\driver\msedgedriver.exe")
        driver = webdriver.Edge(service=service)
    else:
        service = Service("C:\Development\selenium_project\\tests\driver\msedgedriver.exe")
        edge_option = Options()
        edge_option.add_argument("--headless")
        edge_option.add_argument("--disable-gpu")
        edge_option.add_argument("--window-size=1920,1080")
        driver = webdriver.Edge(service=service, options=edge_option)


    driver.maximize_window()
    # Implicit wait الانتظار الضمني
    driver.set_page_load_timeout(30)
    driver.set_script_timeout(30)
    driver.implicitly_wait(30)
    driver.get(url)
    return driver

def quit_driver(driver):
    driver.quit()

def close_current_window(driver):
    driver.close()