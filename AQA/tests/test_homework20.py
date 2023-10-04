import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from utils import helpers, locators
from utils.helpers import provide_value, provide_value_id, is_element_visible, provide_value_name
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest

# Задание 1:
# 1. Открыйть сайт http://thedemosite.co.uk/login.php
# 2. Ввести имя в поле username
# 3. Ввести пароль в поле password
# 4. Нажать на кнопку Test Login
# 5. Проверить, что Successful Login отображаются

site1 = "http://thedemosite.co.uk/login.php"
locator_username = '//*[@id="saveform"]/div/center/table/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/p/input'  # xpath
locator_password = "password"  # name
locator_testlogin_button = "FormsButton2"  # name
locator_title = '/html/body/table/tbody/tr/td[1]/blockquote[1]/blockquote/center/big/font/b'  # xpath
expected_text = 'Successful Login'


def test_exersice1(driver):
    driver.get(site1)
    username_field = driver.find_element(By.XPATH, locator_username)
    username_field.send_keys("username")
    password_field = driver.find_element(By.NAME, locator_password)
    password_field.send_keys("12345678")
    button = driver.find_element(By.NAME, locator_testlogin_button)
    button.click()
    driver.implicitly_wait(5)
    title = driver.find_element(By.XPATH, locator_title)
    try:
        assert title.text == expected_text, f"Текст элемента: {title.text}, ожидался текст: {expected_text}"
    except AssertionError as e:
        logging.error(f"Assertion failed: {str(e)}")


# Задание 2
# 1. Открыть сайт http://demo.guru99.com/test/newtours/register.php
# 2. Заполнить все поля
# 3. Нажать кнопку Submit
# 4. Проверить, что отображается правильно имя и фамилия
# Подсказка xpath ".//tr//table//font[3]”
# 5.Проверить, что отображается правильно username
# Подсказка xpath ".//tr//table//font[5]”

site2 = 'http://demo.guru99.com/test/newtours/register.php'
password = '12345678'
expecetd_name = 'Cecilia Bracamonte'
name_check = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/p[1]/font/b'
username_check = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/p[3]/font/b'


def test_exersice2(driver):
    driver.get(site2)
    provide_value(driver, locators.first_name, 'Cecilia')
    provide_value(driver, locators.last_name, 'Bracamonte')
    provide_value(driver, locators.phone_for_booking, '+5113654943')
    provide_value(driver, locators.email_for_booking, 'cecilia@peru.com')
    provide_value(driver, locators.address, 'Los Nogales 139')
    provide_value(driver, locators.city, 'Lima')
    provide_value(driver, locators.state, 'Lima Province')
    provide_value(driver, locators.postalcode, '02002')
    country = Select(driver.find_element(By.CSS_SELECTOR, locators.country))
    country.select_by_value('PERU')
    provide_value(driver, locators.user_name, 'cecilia')
    provide_value(driver, locators.password, password)
    provide_value(driver, locators.confirm_password, password)

    registration = driver.find_element(By.CSS_SELECTOR, locators.submit)
    registration.click()
    actual_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, name_check)))
    actual_username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, username_check)))
    assert actual_name == expecetd_name, f"Имя: {actual_name}, ожидалось имя: {expecetd_name}"
    assert actual_username == locators.user_name, f"Юзернейм: {actual_username}, ожидался юзернейм: {locators.user_name}"


# Задание 3
# Создать минимум пять тестов для выбранного вами сайта
# Добавить документацию к тестом, чтобы можно было понять о чем тест
site3 = 'https://automationintesting.online/'
email3 = 'hknemzlsyp@mailinator.com'


# test1: лого сайта отобразилось
def test_logo_is_presented(driver):
    driver.get(site3)
    logo = driver.find_element(By.XPATH, locators.logo_url)
    assert logo


# test2: присутствует секция Rooms
expected_title = 'Rooms'


def test_rooms_is_presented(driver):
    driver.get(site3)
    actual_title = driver.find_element(By.XPATH, locators.title_rooms).text
    assert actual_title == expected_title, f"Текущий заголовок: {actual_title}, ожидался заголовок: {expected_title}"


# test3: можно отправить письмо
message = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque imperdiet turpis sed dictum sollicitudin. Mauris malesuada tortor nec consectetur gravida.'
expected_message = 'Thanks for getting in touch Deresse Mekonnen!'

def test_send_email(driver):
    driver.get(site3)
    provide_value_id(driver, locators.name_input, 'Deresse Mekonnen')
    provide_value_id(driver, locators.email_input, 'deresse@mail.com')
    provide_value_id(driver, locators.phone_input, '+251505424878')
    provide_value_id(driver, locators.subject_input, 'Test #3')
    provide_value_id(driver, locators.message_input, message)
    submit_form = driver.find_element(By.ID, locators.submit_button)
    submit_form.click()
    actual_message = driver.find_element(By.XPATH, locators.success_section).text
    assert actual_message == expected_message, f"Текущий текст: {actual_message}, ожидался текст: {expected_message}"


# test4: можно отменить букинг

def test_cancel_booking(driver):
    driver.get(site3)
    book_button = driver.find_element(By.XPATH, locators.book_room_button)
    book_button.click()
    cancel_button = driver.find_element(By.XPATH, locators.cancel_button)
    is_element_visible(driver, cancel_button)
    cancel_button.click()
    assert WebDriverWait(driver, 5).until(
            EC.invisibility_of_element_located((By.XPATH, locators.cancel_button)))


# test5: можно создать букинг комнаты
def test_book_room(driver):
    driver.get(site3)
    book_button = driver.find_element(By.XPATH, locators.book_room_button)
    book_button.click()
    first_date = driver.find_element(By.XPATH, locators.first_date)
    second_date = driver.find_element(By.XPATH, locators.second_date)
    action_chains = ActionChains(driver)
    action_chains.drag_and_drop(first_date, second_date).perform()
    provide_value_name(driver, locators.firstname, 'Arthur')
    provide_value_name(driver, locators.lastname, 'Schopenhauer')
    provide_value_name(driver, locators.email_for_booking, 'arthur@schopenhauer.com')
    provide_value_name(driver, locators.phone_for_booking, '+491522343333')
    book = driver.find_element(By.XPATH, locators.book_button)
    book.click()
    success_message = is_element_visible(driver, locators.success_message)
    assert success_message
