from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
import time

def get_driver(browser: str):
    """Returns a web driver instance based on the selected browser."""
    if browser.lower() == "chrome":
        return webdriver.Chrome()
    elif browser.lower() == "firefox":
        return webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser. Use 'chrome' or 'firefox'.")

# Example usage
if __name__ == "__main__":
    browser_choice = input("Enter the browser (chrome/firefox): ").strip().lower()
    driver = get_driver(browser_choice)

    try:
        # Open a website
        driver.get("http://www.python.org")
        print(f"Page Title: {driver.title}")

        # Example: Finding an element
        example_element = driver.find_element(By.TAG_NAME, "h2")
        print(f"First H2 text: {example_element.text}")
        time.sleep(5)
    finally:
        driver.quit()
