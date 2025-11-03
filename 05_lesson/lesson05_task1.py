from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def test_blue_button():
    print("== ТЕСТ SELENIUM ==")

    # Настройка Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    try:
        # Инициализация драйвера
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Открытие страницы
        driver.get("https://www.saucedemo.com/")

        # Поиск и взаимодействие с элементами
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys("standard_user")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sauce")

        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        # Проверка успешного входа
        WebDriverWait(driver, 10).until(
            EC.url_contains("/inventory.html")
        )

        print("Тест пройден успешно!")

    except Exception as e:
        print(f"Ошибка во время выполнения теста: {e}")

    finally:
        # Закрытие браузера
        if 'driver' in locals():
            driver.quit()


if __name__ == "__main__":
    test_blue_button()
