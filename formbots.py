from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
firefox_options = Options()
firefox_options.add_argument('--head')  # Run in headless mode
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--disable-dev-shm-usage')
firefox_options.add_argument('--disable-gpu')

# Specify the path to GeckoDriver
gecko_driver_path = '/opt/homebrew/bin/geckodriver'  

# Initialize the WebDriver
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service, options=firefox_options)

try:
    # Open the URL
    url = "http://localhost:3000/"
    driver.get(url)
    driver.maximize_window()
    # Allow the page to load
    time.sleep(2)  # Increase sleep time to ensure full page load

    # Fill in the six fields
    field1 = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, 'field1'))
    )
    field1.send_keys("12345678901234")

    field2 = driver.find_element(By.NAME, 'field2')
    field2.send_keys("John Doe")

    field3 = driver.find_element(By.NAME, 'field3')
    field3.send_keys("2024-08-30")
    field4 = driver.find_element(By.NAME, 'field4')
    field4.send_keys("2024-08-30")
    field5 = driver.find_element(By.NAME, 'field5')
    field5.send_keys("2024-08-30")
    field6 = driver.find_element(By.NAME, 'field6')
    field6.send_keys("2024-08-30")


    # Submit the form
    submit_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'sub'))
    )
    submit_button.click()
    
    print("Form submitted successfully.")
    time.sleep(1000)
except Exception as e:
    print(f"An error occurred: {e}")
    driver.save_screenshot("error_screenshot.png")  # Save a screenshot for debugging

finally:
    driver.quit()
