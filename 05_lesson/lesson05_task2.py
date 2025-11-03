from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_dynamic_id_button():
    # Настройка Chrome драйвера
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    try:
        # 1. Открыть браузер Google Chrome
        print("🔄 Открываю браузер Chrome...")

        # 2. Перейти на страницу
        driver.get("http://uitestingplayground.com/dynamicid")
        print("✅ Страница загружена")

        # 3. Найти и кликнуть на синюю кнопку
        blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
        blue_button.click()
        print("✅ Клик на синюю кнопку выполнен")

        # Небольшая пауза чтобы увидеть результат
        time.sleep(2)

        print("🎯 Скрипт выполнен успешно!")

    except Exception as e:
        print(f"❌ Ошибка: {e}")

    finally:
        # Закрыть браузер
        driver.quit()
        print("🔚 Браузер закрыт")


# Запуск скрипта
if __name__ == "__main__":
    test_dynamic_id_button()
