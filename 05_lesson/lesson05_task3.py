from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_browser_input():
    # Настройка Chrome драйвера
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # 1. Открыть браузер Chrome
        print("🔄 Открываю браузер Chrome...")

        # 2. Перейти на страницу
        driver.get("http://the-internet.herokuapp.com/inputs")
        print("✅ Страница загружена")

        # 3. Найти поле ввода
        input_field = driver.find_element(By.TAG_NAME, "input")

        # 4. Ввести в поле текст "Sky"
        input_field.send_keys("Sky")
        print("✅ Текст 'Sky' введен в поле")

        # Небольшая пауза для наглядности
        time.sleep(2)

        # 5. Очистить поле
        input_field.clear()
        print("✅ Поле очищено")

        # Небольшая пауза для наглядности
        time.sleep(2)

        # 6. Ввести в поле текст "Pro"
        input_field.send_keys("Pro")
        print("✅ Текст 'Pro' введен в поле")

        # Небольшая пауза чтобы увидеть результат
        time.sleep(2)

        print("🎯 Скрипт выполнен успешно!")

    except Exception as e:
        print(f"❌ Ошибка: {e}")

    finally:
        # 7. Закрыть браузер
        driver.quit()
        print("🔚 Браузер закрыт")


# Запуск скрипта
if __name__ == "__main__":
    test_browser_input()
