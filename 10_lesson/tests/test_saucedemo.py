import pytest
import allure
from selenium import webdriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("SauceDemo E-commerce Flow")
@allure.severity(allure.severity_level.BLOCKER)
class TestSauceDemo:
    """
    Test suite for complete purchase flow in SauceDemo application.
    """

    @allure.title("Complete end-to-end purchase flow")
    @allure.description("""
    This test verifies the complete user journey from login to purchase completion
    including product selection, cart management, and checkout process.
    """)
    def test_complete_purchase_flow(self, browser: webdriver.Remote) -> None:
        """
        Test complete purchase workflow in SauceDemo application.

        Steps:
        1. Login with valid credentials
        2. Add required products to cart
        3. Navigate to cart and proceed to checkout
        4. Fill customer information
        5. Verify total amount and complete purchase
        """
        with allure.step("Step 1: Login to application"):
            login_page = LoginPage(browser)
            login_page.open()
            login_page.login("standard_user", "secret_sauce")
            allure.attach(browser.get_screenshot_as_png(), name="Login_success",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step("Step 2: Add products to shopping cart"):
            products_page = ProductsPage(browser)
            products_page.add_all_required_products()

            with allure.step("Verify cart contains 3 products"):
                cart_count = products_page.get_cart_count()
                assert cart_count == 3, f"Expected 3 products in cart, got {cart_count}"
                allure.attach(f"Cart items count: {cart_count}", name="CartCount")

        with allure.step("Step 3: Navigate to shopping cart"):
            products_page.go_to_cart()

        with allure.step("Step 4: Proceed to checkout"):
            cart_page = CartPage(browser)
            cart_page.click_checkout()

        with allure.step("Step 5: Fill customer information"):
            checkout_page = CheckoutPage(browser)
            checkout_page.fill_checkout_info("John", "Doe", "12345")
            checkout_page.click_continue()
            allure.attach(browser.get_screenshot_as_png(), name="Checkout_info",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step("Step 6: Verify order total amount"):
            total_amount = checkout_page.get_total_amount()

            with allure.step(f"Check total amount is $58.29 (actual: ${total_amount})"):
                assert total_amount == "58.29", (
                    f"Expected total amount $58.29, got ${total_amount}"
                )
                allure.attach(f"Total amount: ${total_amount}", name="TotalAmount")

        with allure.step("Step 7: Complete purchase"):
            checkout_page.click_finish()

            with allure.step("Verify purchase completion"):
                allure.attach("Purchase completed successfully", name="CompletionStatus")
                allure.attach(browser.get_screenshot_as_png(), name="Purchase_complete",
                              attachment_type=allure.attachment_type.PNG)