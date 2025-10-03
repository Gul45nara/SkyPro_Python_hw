from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_blue_button():
    print("Запуск теста...")

    # Автоматическая установка ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        print("Открываю страницу...")
        driver.get("http://uitestingplayground.com/classattr")

        wait = WebDriverWait(driver, 10)

        print("Ищу кнопку...")
        # Ищем кнопку по тексту
        blue_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Button')]"))
        )

        print(f"Текст кнопки: {blue_button.text}")
        print(f"Классы кнопки: {blue_button.get_attribute('class')}")

        blue_button.click()
        print("Успешно: Кнопка нажата")

        # Обработка alert
        try:
            alert = wait.until(EC.alert_is_present())
            alert_text = alert.text
            alert.accept()
            print(f"Alert закрыт: {alert_text}")
        except:
            print("Alert не появился")

    except Exception as e:
        print(f"Ошибка: {e}")

    finally:
        driver.quit()
        print("Браузер закрыт")


if __name__ == "__main__":
    test_blue_button()