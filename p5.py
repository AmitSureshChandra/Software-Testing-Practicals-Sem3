from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()

try:
    driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")

    driver.find_element(By.ID, "alertexamples").click()  
    alert = Alert(driver)
    print(f"Simple Alert Text: {alert.text}")
    alert.accept()  

    driver.find_element(By.ID, "confirmexample").click()  
    alert = Alert(driver)
    print(f"Confirmation Alert Text: {alert.text}")
    alert.dismiss()  
    
    driver.find_element(By.ID, "promptexample").click()  
    alert = Alert(driver)
    print(f"Prompt Alert Text: {alert.text}")
    alert.send_keys("Selenium Test")  
    alert.accept()  

finally:
    driver.quit()
