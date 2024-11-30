import pyautogui
import time
import random
import string

# Function to generate a random redeem code
def generate_random_code():
    return '-'.join(
        ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        for _ in range(3)
    )

# Simulate the redeem process with retries
def redeem_code_flow():
    while True:
        redeem_code = generate_random_code()
        print(f"Trying code: {redeem_code}")

        # Step 1: Click on the redeem input box
        print("Move your mouse to the redeem input box; press CTRL+C to stop the script.")
        time.sleep(3)
        redeem_input_position = pyautogui.position()  # Place your mouse on the input field
        pyautogui.click(redeem_input_position)
        time.sleep(0.5)

        # Step 2: Enter the redeem code
        pyautogui.typewrite(redeem_code, interval=0.1)
        time.sleep(1)

        # Step 3: Click the redeem button
        print("Move your mouse to the redeem button; press CTRL+C to stop the script.")
        time.sleep(3)
        redeem_button_position = pyautogui.position()  # Place your mouse on the redeem button
        pyautogui.click(redeem_button_position)
        time.sleep(5)  # Wait for response

        # Step 4: Check for an error message (simulating detection)
        print("Move your mouse to the location where an error message might appear; press CTRL+C to stop the script.")
        time.sleep(3)
        error_position = pyautogui.position()  # Point to where the error might appear
        error_screenshot = pyautogui.screenshot(region=(error_position.x, error_position.y, 200, 50))  # Adjust size

        # Simulate error detection (dummy logic)
        error_detected = True  # Assume an error was detected; replace with actual detection logic

        if error_detected:
            print("Error detected! Clearing the input and trying a new code...")
            pyautogui.click(redeem_input_position)  # Click back into the input field
            pyautogui.hotkey("ctrl", "a")  # Select all text
            pyautogui.press("backspace")  # Clear the field
        else:
            print(f"Code {redeem_code} redeemed successfully!")
            break  # Exit the loop on success

# Run the redeem flow
try:
    redeem_code_flow()
except KeyboardInterrupt:
    print("Script stopped manually.")
except Exception as e:
    print(f"An error occurred: {e}")
