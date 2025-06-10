Feature: Tests for Target Website


  Scenario: User can search for a product on Target
    Given Open target main page
    When Search for tea
    Then Verify search worked


  Scenario: 'Your car is empty' message is shown for empty cart
    Given Open target main page
    When Click on cart icon
    Then Verify 'Your cart is empty' message is shown


  Scenario: Logged out user can navigate to sign in page
    Given Open target main page
    When Click account icon
    When Click sign in button
    Then Verify signin form opened