from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
import time


def login_test():
    # Настройка Chrome драйвера
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # 1. Открыть браузер Chrome
        print("🔄 Открываю браузер Chrome...")

        # 2. Перейти на страницу логина
        driver.get("http://the-internet.herokuapp.com/login")
        print("✅ Страница логина загружена")

        # Добавляем ожидание полной загрузки страницы
        wait = WebDriverWait(driver, 10)

        # 3. Найти и ввести username
        username_field = wait.until(
            ec.presence_of_element_located((By.ID, "username"))
        )
        username_field.clear()
        username_field.send_keys("tomsmith")
        print("✅ Логин 'tomsmith' введен")

        # 4. Ввести password
        password_field = driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys("SuperSecretPassword!")
        print("✅ Пароль введен")

        # 5. Нажать кнопку Login
        login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
        login_button.click()
        print("✅ Кнопка Login нажата")

        # 6. Ожидание появления зеленой плашки
        success_message = wait.until(
            ec.visibility_of_element_located((By.ID, "flash"))
        )

        # 7. Вывести текст с зеленой плашки в консоль
        message_text = success_message.text.strip()
        print(f"✅ Текст с зеленой плашки: {message_text}")

        # Небольшая пауза чтобы увидеть результат
        time.sleep(2)

        print("🎯 Скрипт выполнен успешно!")

    except Exception as e:
        print(f"❌ Ошибка: {e}")
        # Сделаем скриншот для отладки
        driver.save_screenshot("login_error.png")
        print("📸 Скриншот ошибки сохранен как 'login_error.png'")

    finally:
        # 8. Закрыть браузер
        driver.quit()
        print("🔚 Браузер закрыт")


# Запуск скрипта
if __name__ == "__main__":
    login_test()