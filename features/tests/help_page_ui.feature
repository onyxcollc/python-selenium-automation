
Feature: Looking to verify UI elements on Target help page


  Scenario: Verify elements on Target Help Page
    Given Go to help page
    Then Verify elements on the page


  Scenario: User can select Help topic Promotions & Coupons
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Promotions & Coupons
    Then Verify help Current promotions page opened


  Scenario: User can select Help topic Payment Options
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Partner Programs
    Then Verify help Ulta Beauty at Target page opened


  Scenario: User can select Help topic Target Account
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Target Account
    Then Verify help Create account page opened