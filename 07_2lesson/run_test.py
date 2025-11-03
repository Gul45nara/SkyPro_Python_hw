from selenium import webdriver
from calculator_page import CalculatorPage
import time


def main():
    print("🚀 Запуск теста калькулятора с PageObject...")

    # Создаем драйвер
    driver = webdriver.Chrome()

    try:
        # Создаем объект страницы
        calculator = CalculatorPage(driver)

        print("1. Открываем страницу калькулятора...")
        calculator.open()

        print("2. Устанавливаем задержку 45 секунд...")
        calculator.set_delay(45)

        print("3. Выполняем операцию 7 + 8...")
        calculator.calculate_7_plus_8()

        print("4. Ожидаем результат (может занять до 45 секунд)...")
        start_time = time.time()
        result = calculator.get_result()
        end_time = time.time()

        execution_time = end_time - start_time
        print(f"5. Получен результат: {result}")
        print(f"Время выполнения: {execution_time:.2f} секунд")

        if result == "15":
            print("✅ ТЕСТ ПРОЙДЕН УСПЕШНО!")
            return True
        else:
            print(f"❌ ТЕСТ НЕ ПРОЙДЕН! Ожидалось '15', получено '{result}'")
            return False

    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")
        return False

    finally:
        print("6. Закрываем браузер...")
        driver.quit()


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
