from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

try:
    driver.get("https://demoqa.com/buttons")  
    
    actions = ActionChains(driver)
    
    right_click_button = driver.find_element(By.ID, "rightClickBtn")
    actions.context_click(right_click_button).perform()
    print("Right-clicked on the button.")
    
    double_click_button = driver.find_element(By.ID, "doubleClickBtn")
    actions.double_click(double_click_button).perform()
    print("Double-clicked on the button.")
    
    driver.get("https://demoqa.com/dragabble")
    draggable_element = driver.find_element(By.ID, "dragBox")
    drop_target = driver.find_element(By.ID, "app")

    actions.drag_and_drop(draggable_element, drop_target).perform()
    print("Dragged the element and dropped it.")

finally:
    driver.quit()
