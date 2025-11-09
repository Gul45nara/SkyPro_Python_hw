from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Локаторы
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CLASS_NAME, "error-message-container")

    def open(self):
        """Открыть страницу логина"""
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        """Выполнить логин - все действия в одном методе"""
        # Заполняем username
        self.driver.find_element(*self.username_field).send_keys(username)
        # Заполняем password
        self.driver.find_element(*self.password_field).send_keys(password)
        # Нажимаем кнопку входа
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        """Получить текст ошибки"""
        error_element = self.wait.until(EC.presence_of_element_located(self.error_message))
        return error_element.text
