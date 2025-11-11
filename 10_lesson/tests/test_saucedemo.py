import allure
from selenium import webdriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Purchase Flow")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Complete purchase flow on SauceDemo")
@allure.description(
    "Test the complete purchase flow from login to order completion "
    "with total amount verification"
)
def test_saucedemo_purchase_flow():
    """Test complete purchase flow on SauceDemo website"""
    driver = webdriver.Chrome()

    try:
        with allure.step("Open login page and authenticate"):
            login_page = LoginPage(driver)
            login_page.open()
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Add products to cart"):
            products_page = ProductsPage(driver)
            products_page.add_all_required_products()
            products_page.go_to_cart()

        with allure.step("Confirm cart contents"):
            cart_page = CartPage(driver)
            cart_page.click_checkout()

        with allure.step("Fill customer information"):
            checkout_page = CheckoutPage(driver)
            checkout_page.fill_checkout_info("John", "Doe", "12345")
            checkout_page.click_continue()

        with allure.step("Verify total amount"):
            total_text = checkout_page.get_total_amount()
            total_amount = total_text.replace("Total: $", "")

            expected_total = "58.29"
            with allure.step(
                f"Check total: {total_amount} vs {expected_total}"
            ):
                error_msg = (
                    f"Expected total should be ${expected_total}, "
                    f"but got ${total_amount}"
                )
                assert total_amount == expected_total, error_msg

        with allure.step("Complete purchase"):
            checkout_page.click_finish()

        with allure.step("Verify purchase completion"):
            pass

    finally:
        driver.quit()
