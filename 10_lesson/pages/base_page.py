from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from typing import Tuple


class BasePage:
    """
    Базовый класс для всех Page Object классов.
    """

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # Увеличил с 10 до 20 секунд

    def find_element(self, locator: Tuple[str, str]) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator: Tuple[str, str]) -> None:
        self.find_element(locator).click()

    def input_text(self, locator: Tuple[str, str], text: str) -> None:
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator: Tuple[str, str]) -> str:
        return self.find_element(locator).text