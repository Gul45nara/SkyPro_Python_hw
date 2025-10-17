from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

try:
    text_input = driver.find_element(By.ID, "newButtonName")
    text_input.clear()
    text_input.send_keys("SkyPro")

    blue_button = driver.find_element(By.ID, "updatingButton")
    blue_button.click()

    button_text = blue_button.text
    print(button_text)

finally:
    driver.quit()
