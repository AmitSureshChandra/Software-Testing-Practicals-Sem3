from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

try:
    driver.get("https://demoqa.com/select-menu")  
    
    dropdown = driver.find_element(By.ID, "oldSelectMenu")
    select = Select(dropdown)

    # Select 'Red' by visible text and assert the selection
    select.select_by_visible_text("Red")
    selected_option = select.first_selected_option
    assert selected_option.text == "Red", f"Expected 'Red', but got {selected_option.text}"
    
    # Select 'Blue' by value and assert the selection
    select.select_by_value("1")
    selected_option = select.first_selected_option
    assert selected_option.text == "Blue", f"Expected 'Blue', but got {selected_option.text}"

finally:
    driver.quit()
