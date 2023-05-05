Feature: Cart and Order Management

Scenario: Accessing the Cart
Given a user is logged in
When the user accesses their cart
Then the cart should be displayed with the correct products and quantities

Scenario: Accessing Orders
Given a user is logged in
When the user accesses their order history
Then the order history should display the correct orders with product information