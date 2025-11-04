from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, username, password):
        username_field = self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

    def get_error_message(self):
        error_element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "error-message-container")))
        return error_element.text
