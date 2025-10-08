from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_dynamic_id_button():
    # Настройка Chrome драйвера
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # 1. Открыть браузер Google Chrome
        print("🔄 Открываю браузер Chrome...")

        # 2. Перейти на страницу
        driver.get("http://uitestingplayground.com/dynamicid")
        print("✅ Страница загружена")

        # 3. Добавляем ожидание загрузки страницы
        wait = WebDriverWait(driver, 10)

        # 4. Ищем кнопку по тексту
        blue_button = wait.until(
            ec.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Button with Dynamic ID')]"))
        )

        # 5. Кликаем на кнопку
        blue_button.click()
        print("✅ Клик на синюю кнопку выполнен")

        # Небольшая пауза чтобы увидеть результат
        time.sleep(2)

        print("🎯 Скрипт выполнен успешно!")

    except Exception as e:
        print(f"❌ Ошибка: {e}")
        # Для отладки: сделаем скриншот
        driver.save_screenshot("error_screenshot.png")
        print("📸 Скриншот ошибки сохранен как 'error_screenshot.png'")

    finally:
        # Закрыть браузер
        driver.quit()
        print("🔚 Браузер закрыт")


# Запуск скрипта
if __name__ == "__main__":
    test_dynamic_id_button()