import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

@pytest.mark.ui
def test_check_incorrect_username():
    #Створення об'єкту для керування браузером
    driver = webdriver.Chrome(
        service=Service(r"D:\QA_GIT\QA_Auto" + r"\chromedriver.exe")
    )

    # відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")

    #Знаходимо поле, в яке будемо вводити неправильне ім'я користувача чи поштову адресу
    login_elem = driver.find_element(By.ID, 'login_field')

    #Вводимо неправильне ім'я користувача або поштову адресу
    login_elem.send_keys("sergiibutenko@mistake.com")

    #Знаходимо поле для введення неправильного паролю
    pass_elem = driver.find_element(By.ID, "password")

    #Вводимо неправильний пароль
    pass_elem.send_keys("wrong password")

    #Знаходимо кнопку sign in
    btn_elem = driver.find_element(By.NAME, "commit")

    #Емулюємо натискання лівої кнопки миші
    btn_elem.click()

    #Перевіряємо, що назва сторінки така, як ми очікеємо
    assert driver.title == "Sign in to GitHub · GitHub"
    time.sleep(3)

    #Закриваємо браузер
    driver.close()
