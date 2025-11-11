from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class BasePage:
    """Base page class with common methods"""

    def __init__(self, driver: webdriver, timeout: int = 10):
        """
        Initialize base page

        Args:
            driver: WebDriver instance
            timeout: timeout in seconds
        """
        self.driver = driver
        self.timeout = timeout

    def find_element(self, locator: tuple, timeout: int = None):
        """
        Find element on page

        Args:
            locator: tuple (By, selector)
            timeout: timeout in seconds

        Returns:
            WebElement: found element
        """
        if timeout is None:
            timeout = self.timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator: tuple, timeout: int = None):
        """
        Find multiple elements on page

        Args:
            locator: tuple (By, selector)
            timeout: timeout in seconds

        Returns:
            list: list of WebElements
        """
        if timeout is None:
            timeout = self.timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
