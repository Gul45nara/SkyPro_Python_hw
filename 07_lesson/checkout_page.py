from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")
        self.finish_button = (By.ID, "finish")

    def enter_first_name(self, first_name):
        """Ввести имя."""
        self.driver.find_element(*self.first_name_input).send_keys(first_name)

    def enter_last_name(self, last_name):
        """Ввести фамилию."""
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

    def enter_postal_code(self, postal_code):
        """Ввести почтовый индекс."""
        element = self.driver.find_element(*self.postal_code_input)
        element.send_keys(postal_code)

    def click_continue(self):
        """Нажать кнопку Continue."""
        self.driver.find_element(*self.continue_button).click()

    def get_total_amount(self):
        """Получить итоговую сумму."""
        total_text = self.driver.find_element(*self.total_label).text
        return total_text

    def fill_checkout_info(self, first_name, last_name, postal_code):
        """Заполнить информацию для оформления заказа."""
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.click_continue()
