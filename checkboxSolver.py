from playwright.sync_api import sync_playwright
import pyautogui
import random
import time


def move_mouse_human_like_system(start_x, start_y, end_x, end_y, steps=30):
    """
    Simulates human-like mouse movements for the system-level cursor
    from (start_x, start_y) to (end_x, end_y).
    """
    x_delta = end_x - start_x
    y_delta = end_y - start_y

    for step in range(steps):
        x = start_x + (x_delta * step / steps) + random.uniform(-0.5, 0.5)
        y = start_y + (y_delta * step / steps) + random.uniform(-0.5, 0.5)
        pyautogui.moveTo(x, y, duration=0.02)  # Moves system-level cursor
        print(f"Moving to: ({x:.2f}, {y:.2f})")  # Debugging intermediate positions

    # Ensure the mouse ends up exactly at the target
    pyautogui.moveTo(end_x, end_y, duration=0.05)
    print(f"Final position adjusted to: ({end_x}, {end_y})")


def solve_captcha_move_to_iframe():
    with sync_playwright() as p:
        # Launch the browser in non-headless mode
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the CAPTCHA demo page
        page.goto("http://localhost:3000/box")

        # Wait for the iframe with title 'reCAPTCHA' to load
        iframe_locator = page.locator("iframe[name='c-ik3z85kzicki']")
        iframe_locator.wait_for(state="visible")  # Wait until iframe is visible

        # Locate the bounding box of the iframe
        iframe_rect = iframe_locator.bounding_box()

        # Ensure the bounding box is not None
        if not iframe_rect:
            print("Failed to locate the reCAPTCHA iframe.")
            browser.close()
            return

        # Calculate the center coordinates of the iframe
        target_x = iframe_rect['x'] + iframe_rect['width'] / 2
        target_y = iframe_rect['y'] + iframe_rect['height'] / 2

        print(f"Target coordinates: {target_x:.2f}, {target_y:.2f}")  # Debug log

        # Get the current position of the mouse
        current_mouse_position = pyautogui.position()
        start_x, start_y = current_mouse_position.x, current_mouse_position.y

        # Move the mouse in a human-like way to the iframe
        move_mouse_human_like_system(start_x, start_y, target_x, target_y)

        # Click the iframe (system-level click)
        pyautogui.click()
        print("Mouse moved to and clicked on the iframe.")

        # Add a delay to observe the result
        time.sleep(20)

        browser.close()


# Run the function
solve_captcha_move_to_iframe()
