from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from conftest import driver


def provide_value(driver, locator, text):
    element = driver.find_element(By.CSS_SELECTOR, locator)
    element.send_keys(text)


def provide_value_id(driver, locator, text):
    element = driver.find_element(By.ID, locator)
    element.send_keys(text)


def provide_value_name(driver, locator, text):
    element = driver.find_element(By.NAME, locator)
    element.send_keys(text)


def is_element_visible(driver, locator):
    try:
        return WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locator))
        )
    except:
        return "Element is not found"
