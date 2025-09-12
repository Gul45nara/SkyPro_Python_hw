from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def test_blue_button():
    # Настройки Chrome для стабильной работы
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")

    # Инициализация драйвера Chrome
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Установим таймаут ожидания элементов
        driver.implicitly_wait(10)

        # Открытие страницы
        print("Открываю страницу...")
        driver.get("http://uitestingplayground.com/classattr")

        # Поиск и клик по синей кнопке
        print("Ищу синюю кнопку...")
        blue_button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")
        blue_button.click()

        print("Успешно: Клик по синей кнопке выполнен!")

        # Небольшая пауза чтобы увидеть результат
        time.sleep(3)

    except Exception as e:
        print(f"Ошибка: {e}")

    finally:
        # Закрытие браузера
        driver.quit()
        print("Браузер закрыт")


if __name__ == "__main__":
    test_blue_button()