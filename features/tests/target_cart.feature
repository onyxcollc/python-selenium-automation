Feature: Tests For Target Shopping Cart

  Scenario: 'Your car is empty' message is shown for empty cart
    Given Open target main page
    When Click on cart icon
    Then Verify 'Your cart is empty' message is shown
