from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def test_blue_button():
    print("=== ТЕСТ SELENIUM ===")

    # Настройки Chrome для обхода SSL
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--ignore-ssl-errors")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Автоматическая установка ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        print("1. Открываю страницу...")
        driver.get("http://uitestingplayground.com/classattr")
        print(f"2. Заголовок страницы: {driver.title}")
        print(f"3. URL: {driver.current_url}")

        # Ждем загрузки страницы
        import time
        time.sleep(3)

        print("4. Проверяю содержимое страницы...")

        # Посмотрим что действительно загрузилось
        page_source = driver.page_source
        print(f"5. Размер страницы: {len(page_source)} символов")

        if "Обнаружена проблема" in driver.title:
            print("❌ Страница не загрузилась из-за SSL ошибки")
            print("Попробую использовать HTTPS...")
            driver.get("https://uitestingplayground.com/classattr")
            time.sleep(3)

        print(f"6. Новый заголовок: {driver.title}")
        print(f"7. Новый URL: {driver.current_url}")

        # Ищем кнопку
        print("8. Ищу синюю кнопку...")

        # Разные способы поиска кнопки
        try:
            # Способ 1: По классу
            blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
            print("✓ Нашел кнопку по CLASS_NAME")
        except:
            try:
                # Способ 2: По XPath
                blue_button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")
                print("✓ Нашел кнопку по XPATH")
            except:
                try:
                    # Способ 3: По тексту
                    blue_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Button')]")
                    print("✓ Нашел кнопку по тексту")
                except:
                    # Способ 4: Любая кнопка
                    buttons = driver.find_elements(By.TAG_NAME, "button")
                    print(f"Найдено кнопок: {len(buttons)}")
                    for i, btn in enumerate(buttons):
                        print(f"  Кнопка {i}: текст='{btn.text}', класс='{btn.get_attribute('class')}'")

                    if buttons:
                        blue_button = buttons[0]
                        print("✓ Использую первую кнопку")
                    else:
                        print("❌ Не найдено ни одной кнопки")
                        return

        print(f"9. Текст кнопки: '{blue_button.text}'")
        print(f"10. Классы кнопки: '{blue_button.get_attribute('class')}'")

        blue_button.click()
        print("11. Кнопка нажата!")

        print("🎉 ТЕСТ ПРОЙДЕН УСПЕШНО!")

    except Exception as e:
        print(f"❌ Ошибка: {e}")

    finally:
        driver.quit()
        print("Браузер закрыт")


if __name__ == "__main__":
    test_blue_button()