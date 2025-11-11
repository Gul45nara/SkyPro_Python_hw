import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    """WebDriver setup and teardown"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
