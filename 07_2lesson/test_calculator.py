import time
from selenium import webdriver
from calculator_page import CalculatorPage

def main():
    driver = webdriver.Chrome()

    try:
        # Открыть страницу калькулятора
        driver.get("https://erikh123.github.io/simple-calculator/")
        calculator_page = CalculatorPage(driver)

        # Установить задержку 45 секунд
        calculator_page.set_delay(45)

        # Засечь время начала вычислений
        start_time = time.time()

        # Выполнить вычисление 7 + 8
        calculator_page.click_calculator_button("7")
        calculator_page.click_calculator_button("+")
        calculator_page.click_calculator_button("8")
        calculator_page.click_calculator_button("=")

        # Получить результат
        result = calculator_page.get_result()

        # Засечь время окончания вычислений
        end_time = time.time()
        execution_time = end_time - start_time

        # Проверить результат вычислений
        assert result == "15", f"Ожидался результат 15, получен {result}"

        # Проверить время выполнения (примерно 45 секунд с небольшим допуском)
        assert execution_time >= 45, f"Ожидалось время выполнения не менее 45 секунд, получено {execution_time:.2f} секунд"

    finally:
        driver.quit()

if __name__ == "__main__":
    main()