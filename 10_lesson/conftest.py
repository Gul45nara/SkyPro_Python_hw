import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser():
    """
    Pytest fixture for WebDriver initialization and teardown.
    """
    options = Options()

    # Раскомментируй для отладки (чтобы видеть браузер)
    # options.add_argument("--headless")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")

    # Используем webdriver-manager для автоматической установки правильной версии
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.implicitly_wait(30)
    driver.set_page_load_timeout(60)

    yield driver

    # Скриншот при падении теста
    if hasattr(pytest, "test_failed") and pytest.test_failed:
        allure.attach(driver.get_screenshot_as_png(),
                      name="test_failure",
                      attachment_type=allure.attachment_type.PNG)

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        pytest.test_failed = True
    else:
        pytest.test_failed = False