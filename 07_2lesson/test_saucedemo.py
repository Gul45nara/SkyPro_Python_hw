import pytest
from login_page import LoginPage


class TestSauceDemo:
    def test_successful_login(self, driver):
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Простая проверка через assert
        assert "inventory" in driver.current_url

    def test_failed_login(self, driver):
        login_page = LoginPage(driver)
        login_page.login("invalid_user", "wrong_password")

        # Простая проверка ошибки
        error_message = login_page.get_error_message()
        assert "Username and password do not match" in error_message
