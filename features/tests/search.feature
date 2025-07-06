Feature: Tests for Target Search

  @smoke
  Scenario: User can search for tea on Target
    Given Open target main page
    When Search for tea
    And Click search button
    Then Verify search worked for tea

  Scenario: User can search for coffee on Target
    Given Open target main page
    When Search for coffee
    And Click search button
    Then Verify search worked for coffee

  Scenario: User can search for mug on Target
    Given Open target main page
    When Search for mug
    And Click search button
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


  Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for xbox controller
    Then Verify that every product has a name and an image



  Scenario: User can see favorites tooltip for search results
    Given Open target main page
    When Search for tea
    And Hover over favorites icon
    Then Favorites tooltip is shown