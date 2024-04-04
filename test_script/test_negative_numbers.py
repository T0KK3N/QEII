import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestNegativeNumbers(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_negative_numbers(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")
        
        # Find the input fields and enter negative numbers
        fields = ['product-a', 'product-b', 'product-c', 'product-d']
        for field in fields:
            input_field = driver.find_element(By.ID, field)
            input_field.clear()  # Clear any existing value
            input_field.send_keys("-5")

            # Trigger the validation message by removing focus from the input field
            input_field.click()

        # Find and click the calculate button
        calculate_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        calculate_button.click()
        
        # Wait for the validation messages to appear
        time.sleep(2)

        # Find the input fields and retrieve their validation message attributes
        validation_messages = {}
        for field in fields:
            input_field = driver.find_element(By.ID, field)
            validation_messages[field] = input_field.get_attribute("validationMessage")

        # Assert if any validation message attribute is not empty
        for field, message in validation_messages.items():
            self.assertNotEqual(message, "", f"Validation message for {field} is not displayed.")
            print(field, message)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
