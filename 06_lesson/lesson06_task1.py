from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

try:
    # Находим и нажимаем на синюю кнопку
    blue_button = driver.find_element(By.ID, "ajaxButton")
    blue_button.click()

    # Ждем появления зеленой плашки с классом bg-success
    green_banner = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "bg-success"))
    )

    # Получаем текст из зеленой плашки
    text = green_banner.text
    print(text)

finally:
    # Закрываем браузер
    driver.quit()
