Feature: Tests For Target Shopping Cart

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When Click on cart icon
    Then Verify 'Your cart is empty' message is shown
    Then Verify Cart page opened

  Scenario: User can add a product to cart
    Given Open target main page
    When Search for mug
    And Click search button
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has $16.99 subtotal1 item item(s)
    And Verify cart has correct product
