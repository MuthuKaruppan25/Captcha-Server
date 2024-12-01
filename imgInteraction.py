from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import base64
from PIL import Image
from io import BytesIO
import time

def handle_alert(driver, wait_time=5):
    try:
        WebDriverWait(driver, wait_time).until(EC.alert_is_present())
        alert = Alert(driver)
        print("Alert detected. Dismissing the alert.")
        alert.dismiss()  # Use `alert.accept()` to click "OK" if necessary
    except:
        print("No alert detected.")

try:
    # Step 1: Set up Selenium WebDriver for Firefox
    firefox_options = Options()
    firefox_options.set_preference("dom.webnotifications.enabled", False)  # Disable notifications if needed
    gecko_driver_path = '/opt/homebrew/bin/geckodriver'  # Adjust the path to your geckodriver
    firefox_service = Service(gecko_driver_path)
    driver = webdriver.Firefox(service=firefox_service, options=firefox_options)

    # Step 2: Open the web page with the canvas
    driver.get("http://localhost:3000/box")
    time.sleep(5)  # Allow some time for the page to load fully

    # Step 3: Explicitly wait for the canvas element to be present
    canvas = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "canvas"))
    )
    if not canvas:
        raise Exception("Canvas element not found!")

    # Check if the canvas is visible and interactable
    if not canvas.is_displayed():
        raise Exception("Canvas element is not visible!")

    # Step 4: Extract canvas data as base64 using JavaScript
# Step 4: Extract canvas data as base64 using JavaScript with delays after each line
    image_data_url = driver.execute_async_script("""
        var canvas = arguments[0];
        if (canvas) {
            var delay = function(ms) {
                return new Promise(resolve => setTimeout(resolve, ms));
            };

            delay(1000).then(() => {
                console.log("Canvas element found.");

                delay(2000).then(() => {
                    var dataUrl = canvas.toDataURL('image/png');
                    console.log('Canvas data URL:', dataUrl);

                    delay(5000).then(() => {
                        arguments[1](dataUrl);  // Return dataUrl to the Selenium script
                    });
                });
            });
        } else {
            console.error('Canvas element is not found or is invalid.');
            arguments[1](null);  // Return null to the Selenium script
        }
    """, canvas)


    # Step 3: Check if the data URL is valid
    if not image_data_url:
        raise Exception("Failed to extract canvas data!")
    time.sleep(15)
    # Step 5: Decode the base64 string and save the image
    image_data = base64.b64decode(image_data_url.split(",")[1])
    image = Image.open(BytesIO(image_data))
    image.save("captcha_image.png")
    print("CAPTCHA image saved as 'captcha_image.png'.")

    # Optional: Interact with the canvas
    ActionChains(driver).move_to_element(canvas).click().perform()
    print("Simulated click on the canvas.")

except Exception as e:
    print(f"An error occurred: {e}")
    handle_alert(driver)  # Handle unexpected alerts before saving the screenshot
    try:
        driver.save_screenshot("error_screenshot.png")  # Save a screenshot for debugging
        print("Screenshot saved as 'error_screenshot.png'.")
    except Exception as screenshot_error:
        print(f"Failed to save screenshot: {screenshot_error}")

finally:
    driver.quit()
