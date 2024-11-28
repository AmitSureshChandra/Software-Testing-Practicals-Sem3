from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
    
driver = webdriver.Chrome()

try:
    driver.get("https://www.python.org/")
    print(f"Opened URL: {driver.current_url}")

    title = driver.title
    print(f"Page Title: {title}")

    current_url = driver.current_url
    print(f"Current URL: {current_url}")

    driver.maximize_window()
    print("Browser window maximized")

    driver.minimize_window()
    print("Browser window minimized")

    driver.refresh()
    print("Page refreshed")

    driver.get("https://www.google.com")
    print(f"Navigated to: {driver.current_url}")

    driver.back()
    print(f"After going back, URL: {driver.current_url}")

    driver.forward()
    print(f"After going forward, URL: {driver.current_url}")
    
    page_source = driver.page_source
    print(f"Page source length: {len(page_source)} characters")

    driver.get("https://www.example.com")
    element = driver.find_element(By.TAG_NAME, "h1")
    print(f"Found element text: {element.text}")

    
finally:
    driver.quit()
    print("Browser closed")
