import selenium
from selenium import webdriver
driver = webdriver.Chrome()
import pytest

#создаю фикстуру:

@pytest.fixture
def sumple_user():
    options = options()
    options.add_argument("--headless")  # run without UI
    options.add_argument("--no-sandbox")  # required in many CI environments
    options.add_argument("--disable-dev-shm-usage")  # overcome limited /dev/shm size on Linux
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
yield driver
driver.quit()

# успешная авторизация:
    
from selenium.wwebsumple_user.common.by import By
LOGIN_URL = "https://the-internet.herokuapp.com/login"
def test_successful_login(sumple_user):
    sumple_user.get(LOGIN_URL)
    sumple_user.find_element(By.ID, "login").send_keys("tomsmith")
    sumple_user.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    sumple_user.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    success_message = sumple_user.find_element(By.CSS_SELECTOR, ".flash.success")
    assert "Welcome to the Secure Area. When you are done click logout below." in message.text

 # не успешная автоизация:

def  test_unsuccessful_login(user):
    user.get(LOGIN_URL)
    user.find_element(By.ID, "login").send_keys("prosto1")
    user.find_element(By.ID, "password").send_keys("nepassword")
    user.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    error_message = user.find_element(By.CSS_SELECTOR, ".flash.error")
    assert "This is where you can log into the secure area. Enter tomsmith for the username and SuperSecretPassword! for the password. If the information is wrong you should see error messages." in error_message.text
