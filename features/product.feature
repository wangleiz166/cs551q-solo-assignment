Feature: Product Management

Scenario: Displaying Product List
    Given a user is logged in
    When the user accesses the product list
    Then the product list should be displayed with the correct products and quantities