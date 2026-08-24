# Automated E-Commerce Checkout Testing Report

## Project Information

- Project Name: E-Commerce Checkout Flow
- Testing Type: Automated UI Testing
- Tool Used: Selenium WebDriver
- Website: SauceDemo
- Tested By: Vinutha H C
- Date: August 2026

## Objective

To automate and verify the complete e-commerce checkout flow including login, adding a product to the cart, checkout form submission, and successful order confirmation.

## Test Scenarios

### TC-01 Login
- Enter valid username and password.
- Expected Result: User successfully logs in.
- Status: Pass

### TC-02 Add Product to Cart
- Select Sauce Labs Backpack and add it to the cart.
- Expected Result: Product is added to the cart.
- Status: Pass

### TC-03 Open Cart
- Open the shopping cart.
- Expected Result: Selected product is displayed.
- Status: Pass

### TC-04 Checkout Form
- Enter first name, last name, and postal code.
- Expected Result: Form accepts valid details.
- Status: Pass

### TC-05 Complete Order
- Continue to the overview page and click Finish.
- Expected Result: Order is completed successfully.
- Status: Pass

### TC-06 Verify Success Message
- Verify the order confirmation message.
- Expected Result: "Thank you for your order!"
- Status: Pass

## Page Transition Verification

The following page transitions were verified:

Login → Products → Cart → Checkout → Overview → Order Confirmation

All required page transitions were successful.

## Form Validation

Valid customer details were entered during checkout. The checkout form accepted the required information successfully.

## Issues Encountered

No major issues were encountered during the automated checkout test.

## Conclusion

The e-commerce checkout flow was successfully automated using Selenium WebDriver. Login, product selection, cart navigation, checkout form submission, and order confirmation were verified successfully.
