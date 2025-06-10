Feature: Test to verify sign in page
  A logged out user should be able to
  navigate to the Sign in page

  Scenario: Logged out user can navigate to sign in page
    Given Open main page
    When Click account icon
    When Click sign in button
    Then Verify signin form opened