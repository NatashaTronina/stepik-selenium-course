from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    # Нажимаем на кнопку
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    # Принимаем confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # Находим значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # Вычисляем значение y
    y = calc(x)

    # Вводим значение y в поле ответа
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # Даем время скопировать код
    time.sleep(20)
    # Закрываем браузер
    browser.quit()