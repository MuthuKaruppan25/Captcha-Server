import pyautogui
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.webdriver.common.keys import Keys
# Set up Firefox options
firefox_options = Options()
firefox_options.add_argument('--head')  # Comment out to see browser actions
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--disable-dev-shm-usage')
firefox_options.add_argument('--disable-gpu')

# Specify the path to GeckoDriver
gecko_driver_path = '/opt/homebrew/bin/geckodriver'  # Update this path if necessary

# Function to move the mouse using pyautogui
def pyautogui_move_to_element2(driver, element, duration=2.0):
    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(1)  # Allow some time for the page to scroll
    
    # Get the element's position and size relative to the viewport using JavaScript
    element_rect = driver.execute_script("""
        var rect = arguments[0].getBoundingClientRect();
        return {x: rect.left, y: rect.top, width: rect.width, height: rect.height};
    """, element)
     
    # Calculate the center of the element
    target_x = element_rect['x']+30+random.uniform(2, 10)
    target_y = element_rect['y']+125+random.uniform(1, 5)
    print(target_x,target_y)

    # Adjust the target coordinates to account for the browser window's position
    final_x =  target_x
    final_y =  target_y
    duration = random.uniform(0.001, 0.0001)
    # Move the mouse to the element's center and click
    pyautogui.moveTo(final_x, final_y, duration=duration)
    time.sleep(2)
    pyautogui.click()
def pyautogui_move_to_element(driver, element, duration=2.0):
    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(1)  # Allow some time for the page to scroll
    
    # Get the element's position and size relative to the viewport using JavaScript
    element_rect = driver.execute_script("""
        var rect = arguments[0].getBoundingClientRect();
        return {x: rect.left, y: rect.top, width: rect.width, height: rect.height};
    """, element)
     
    # Calculate the center of the element
    target_x = element_rect['x']+30+random.uniform(2, 200)
    target_y = element_rect['y']+120+random.uniform(1, 5)
    print(target_x,target_y)

    # Adjust the target coordinates to account for the browser window's position
    final_x =  target_x
    final_y =  target_y
    duration = random.uniform(0.001, 0.0001)
    # Move the mouse to the element's center and click
    pyautogui.moveTo(final_x, final_y, duration=duration)
    time.sleep(random.uniform(0.001,0.001))
    pyautogui.click()
def pyautogui_move_to_element1(x,y, duration=2.0):

    time.sleep(1)  
    target_x =  x
    target_y = y
    final_x =  target_x
    final_y =  target_y
    duration = random.uniform(0.0001, 1.0)
    pyautogui.moveTo(final_x, final_y, duration=duration)
    
# Initialize the WebDriver in a loop
def sendk(s,t):
    for c in t:
        s.send_keys(c)
        time.sleep(random.uniform(0.0001, 0.01))
        if random.random() <0.1:
            s.send_keys(Keys.BACK_SPACE)
            time.sleep(random.uniform(0.0001, 0.001))
            s.send_keys(c)
        time.sleep(random.uniform(0.0001, 0.01))

while True:
    try:
        service = Service(gecko_driver_path)
        driver = webdriver.Firefox(service=service, options=firefox_options)

        # Open the URL
        url = "http://localhost:3000"
        driver.get(url)
        driver.maximize_window()
        # Allow the page to load
        time.sleep(3)  # Increased sleep time to ensure full page load
        pyautogui_move_to_element1(random.uniform(0, 1200),random.uniform(0, 200), duration=2.0)
        pyautogui_move_to_element1(random.uniform(0, 1200),random.uniform(0, 200), duration=2.0)
        try:
            # Locate the mobile number input field using class selector
            field1 = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.NAME, 'field1'))
            )
            sendk(field1,"12345678901234")
            
          
            pyautogui_move_to_element1(random.uniform(0, 1200),random.uniform(0, 400), duration=2.0)
            pyautogui_move_to_element1(random.uniform(0, 1200),random.uniform(0, 200), duration=2.0)
            field2 = driver.find_element(By.NAME, 'field2')
            pyautogui_move_to_element(driver, field2, duration=2.0)
            sendk(field2,"John Doe")
            time.sleep(random.uniform(0, 0.08))
            field3 = driver.find_element(By.NAME, 'field3')
            pyautogui_move_to_element(driver, field3, duration=2.0)
            sendk(field3,"2024-08-30")
            time.sleep(random.uniform(0, 0.08))
            field4 = driver.find_element(By.NAME, 'field4')
            pyautogui_move_to_element(driver, field4, duration=2.0)
            sendk(field4,"9597959097")
            time.sleep(random.uniform(0, 0.08))
            field5 = driver.find_element(By.NAME, 'field5')
            pyautogui_move_to_element(driver, field5, duration=2.0)
            sendk(field5,"Piramuthu")
            time.sleep(random.uniform(0, 0.0008))
            field6 = driver.find_element(By.NAME, 'field6')
            pyautogui_move_to_element(driver, field6, duration=2.0)
            sendk(field6,"ABCDE1234F")
            # Use pyautogui to move the mouse to the mobile field and click
            # time.sleep(1)  # Simulate a pause before interaction
            time.sleep(5)

            # Locate the "Request OTP" button using class selector
            submit_button = WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'sub'))
                )
            pyautogui_move_to_element1(random.uniform(0, 1200),random.uniform(0, 200), duration=2.0)
            pyautogui_move_to_element1(random.uniform(0, 1200),random.uniform(0, 200), duration=2.0)
            pyautogui_move_to_element1(random.uniform(0, 1200),random.uniform(0, 200), duration=2.0)



            # Use pyautogui to move the mouse to the button and click
            pyautogui_move_to_element2(driver, submit_button, duration=2.0)
            time.sleep(1000)  
            # Simulate a short delay before the click

            print("OTP request sent.")
          

        except Exception as e:
            print(f"An error occurred: {e}")
            driver.save_screenshot("error_screenshot.png")  
            
    finally:
        driver.quit()

