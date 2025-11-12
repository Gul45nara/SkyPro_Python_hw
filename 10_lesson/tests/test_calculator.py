import time
import pytest
import allure
from selenium import webdriver
from pages.calculator_page import CalculatorPage


@allure.feature("Calculator Operations")
@allure.severity(allure.severity_level.CRITICAL)
class TestCalculator:
    """
    Test suite for calculator functionality with delay operations.
    """

    @allure.title("Test calculator operation with 45 seconds delay")
    @allure.description("""
    This test verifies that calculator correctly performs addition operation 
    with specified delay and returns correct result after waiting period.
    """)
    def test_calculator_with_delay(self, browser: webdriver.Remote) -> None:
        """
        Test calculator addition operation with delay verification.

        Steps:
        1. Open calculator page
        2. Set calculation delay to 45 seconds
        3. Perform 7 + 8 operation
        4. Verify result is 15
        5. Verify execution time is at least 45 seconds
        """
        with allure.step("Open calculator application"):
            calculator_page = CalculatorPage(browser)
            calculator_page.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
            allure.attach(browser.get_screenshot_as_png(), name="Calculator_page",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step("Set calculation delay to 45 seconds"):
            calculator_page.set_delay(45)

        with allure.step("Perform addition operation: 7 + 8"):
            start_time = time.time()

            calculator_page.click_calculator_button("7")
            calculator_page.click_calculator_button("+")
            calculator_page.click_calculator_button("8")
            calculator_page.click_calculator_button("=")

            end_time = time.time()
            execution_time = end_time - start_time

        with allure.step("Verify calculation result"):
            result = calculator_page.get_result()

            with allure.step(f"Check result is 15 (actual: {result})"):
                assert result == "15", f"Expected result 15, got {result}"
                allure.attach(f"Calculation result: {result}", name="Result")

        with allure.step("Verify execution time meets delay requirement"):
            with allure.step(f"Check execution time ≥45 seconds (actual: {execution_time:.2f}s)"):
                assert execution_time >= 45, (
                    f"Expected execution time ≥45 seconds, got {execution_time:.2f} seconds"
                )
                allure.attach(f"Execution time: {execution_time:.2f}s", name="ExecutionTime")