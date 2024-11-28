from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/nested_frames")  
    driver.switch_to.frame(1)
    print("Switched to the second frame")
    first_frame_element = driver.find_element(By.TAG_NAME, "body")
    print(f"Text in second frame: {first_frame_element.text}")
    print("Frame handling successful!")
    time.sleep(5)
finally:
    driver.quit()
