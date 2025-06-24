Feature: Tests for logged out user can navigate Sign in page


  Scenario: Logged out user can navigate to sign in page
    Given Open target main page
    When Click account icon
    When Click sign in button
    Then Verify sign in result



  Scenario: User logging into Target Website
    Given Open target main page
    When Click account icon
    When Click sign in button
    And Enter email onyxcollc@gmail.com
    When Click continue button
    # And Click enter your password
    When Enter your Childish
    And Click sign in with password
    #Then Verify login


  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open sign in page
    And Store original window
    When Click Terms and Conditions link
    And Switch to new window
    Then Verify Terms and Conditions page is opened
    And Close current page
    And Return to original window
