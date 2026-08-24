from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Add product to cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

# Open cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

# Checkout
driver.find_element(By.ID, "checkout").click()

# Customer details
driver.find_element(By.ID, "first-name").send_keys("Vinutha")
driver.find_element(By.ID, "last-name").send_keys("HC")
driver.find_element(By.ID, "postal-code").send_keys("577001")

# Continue
driver.find_element(By.ID, "continue").click()

# Finish order
driver.find_element(By.ID, "finish").click()

# Verify success message
success = driver.find_element(By.CLASS_NAME, "complete-header").text
assert success == "Thank you for your order!"

print("Checkout Test Passed")

driver.quit()
