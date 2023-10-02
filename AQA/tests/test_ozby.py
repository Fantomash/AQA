from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest

locator_logo = 'search-top'
support_logo = '//*[@id="top-page"]/header/div[1]/div/a[1]/span'


class TestOzby:

    def test_open_page(self, driver):
        driver.get("https://oz.by/")
        click_logo = driver.find_element(By.ID, locator_logo)
        driver.save_screenshot('open_page.jpg')
        assert WebDriverWait(driver, 5).until(EC.visibility_of(click_logo))
