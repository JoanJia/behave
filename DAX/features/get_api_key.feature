Feature: getAPI_KEY

  Scenario: getAPI_KEY
    Given I am logged dax
    When I make a GET request to "/api/v2/api_key/"
    Then the response status should be 200
    And the response body should contain "results"
