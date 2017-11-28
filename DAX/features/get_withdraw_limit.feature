Feature: getAPI withdraw limit

  Scenario: get withdraw limit
    Given I am logged dax
    And I set "Content-Type" header to "application/json"
    When I make a GET request to "/api/v2/withdraw_limit"
    Then the response status should be 200
    And the response body should contain "remaining"
