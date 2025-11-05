from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")
        self.finish_button = (By.ID, "finish")

    def fill_checkout_info(self, first_name, last_name, postal_code):
        """Простое заполнение информации о покупателе"""
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.postal_code_field).send_keys(postal_code)

    def click_continue(self):
        """Нажать кнопку Continue"""
        self.driver.find_element(*self.continue_button).click()

    def click_finish(self):
        """Нажать кнопку Finish"""
        self.driver.find_element(*self.finish_button).click()

    def get_total_amount(self):
        """Получить итоговую сумму"""
        total_text = self.driver.find_element(*self.total_label).text
        return total_text