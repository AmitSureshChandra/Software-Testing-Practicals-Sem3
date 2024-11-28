from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Firefox()

try:
    driver.get("https://demoqa.com/radio-button")  

    radio_button_yes = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
    
    if not radio_button_yes.is_selected():  
        radio_button_yes.click()
        print("Selected the 'Yes' radio button")

    is_selected = radio_button_yes.is_selected()
    print(f"Is 'Yes' radio button selected? {is_selected}")
    
    radio_button_disabled = driver.find_element(By.ID, "noRadio")
    is_enabled = radio_button_disabled.is_enabled()
    print(f"Is 'No' radio button enabled? {is_enabled}")

    driver.get("https://demoqa.com/checkbox")

    expand_button = driver.find_element(By.CLASS_NAME, "rct-option-expand-all")
    expand_button.click()
    
    checkbox = driver.find_element(By.XPATH, "//label[@for='tree-node-home']")  
    if not checkbox.is_selected():  
        checkbox.click()
        print("Checked the 'Home' checkbox")

    
    checkbox_status = driver.find_element(By.ID, "tree-node-home")
    print(f"Is 'Home' checkbox selected? {checkbox_status.is_selected()}")

    time.sleep(5)
finally:
    driver.quit()
