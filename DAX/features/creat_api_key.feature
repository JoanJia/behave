Feature: create api key

  Scenario: create api key
    Given I am logged dax
    And I set "Content-Type" header to "application/json"
    When I make a POST request to "/api/v2/api_key/"
    """
    {
        "description": "test"
    }
    """
    Then the response status should be 201
    And the response body should contain "access_key"
