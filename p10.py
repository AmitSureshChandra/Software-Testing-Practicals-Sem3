from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

def test_login(username, password):
    driver.get("http://127.0.0.1:5500/p10.html") 
    
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    
    username_field.clear()
    password_field.clear()
    username_field.send_keys(username)
    password_field.send_keys(password)

    password_field.send_keys(Keys.RETURN)

    try:
        username_error = driver.find_element(By.ID, "usernameError")
        password_error = driver.find_element(By.ID, "passwordError")
        print(f"Username: {username}, Password: {password}")
        if username_error.is_displayed() or password_error.is_displayed():
            print("Error found:", username_error.text if username_error.is_displayed() else password_error.text)
            assert username_error.is_displayed() or password_error.is_displayed(), f"Expected error message, but got none for Username: {username}, Password: {password}"
        else:
            print("Login successful!")
            assert not username_error.is_displayed() and not password_error.is_displayed(), f"Expected successful login, but got error for Username: {username}, Password: {password}"
    except Exception as e:
        if e.alert_text:
            print(f"Message: {e.alert_text}")
        else:
            print(f"Error: {e}")

# Define test cases based on equivalence partitioning
test_cases = [
    ("validUser", "validPassword1"), 
    ("usr", "validPassword1"),       
    ("validUser123456", "validPassword1"), 
    ("validUser", "pass"),           
    ("validUser", "verylongpassword12345"), 
    ("usr", "pass")                  
]

# Run the test cases
for username, password in test_cases:
    test_login(username, password)

# Close the browser
driver.quit()
