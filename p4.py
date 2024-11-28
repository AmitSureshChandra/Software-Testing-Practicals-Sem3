from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://unsplash.com/login?referrer=%2F")  

    username_input = driver.find_element(By.NAME, "email")  
    username_input.send_keys("test_user")  
    password_input = driver.find_element(By.CSS_SELECTOR, "input[type='password']")  
    password_input.send_keys("secure_password")
    login_button = driver.find_element(By.XPATH, "//button[text()='Login']")  
    print(f"Login button text: {login_button.text}")

    username_input.clear()
    username_input.send_keys("new_test_user")
    login_button.click()
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")  
    submit_button.click()
    print(f"Current URL after submission: {driver.current_url}")

finally:
    driver.quit()
