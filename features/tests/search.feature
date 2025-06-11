Feature: Tests for Target Search


  Scenario: User can search for tea on Target
    Given Open target main page
    When Search for tea
    Then Verify search worked for tea

  Scenario: User can search for coffee on Target
    Given Open target main page
    When Search for coffee
    Then Verify search worked for coffee

  Scenario: User can search for mug on Target
    Given Open target main page
    When Search for mug
    Then Verify search worked for mug


#  Scenario Outline: User can Search for product
#    Given Open target main page
#    When Search for <search_word>
#    Then Verify search worked for <expected_result>
#    Examples:
#    |search_word |expected_result |
#    |tea         |tea             |
#    |mug         |mug             |
#    |coffee      |coffee          |