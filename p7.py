from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.implicitly_wait(10)  
    
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_button.click()
    
    loaded_text = driver.find_element(By.CSS_SELECTOR, "#finish h4")
    print(f"Dynamically loaded text: {loaded_text.text}")
finally:
    driver.quit()
