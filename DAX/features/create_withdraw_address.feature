Feature: Create new withdraw address

  Scenario:  Create a new btc withdraw address
    Given I am logged dax
    And I set "Content-Type" header to "application/json"
    When I make a POST request to "/api/v2/withdraw_address/"
    """
    {
        "coin_type": "BTC",
        "address": "mmA4ND54mYy73G3eAifHLNxB2z4YKeDu2J"
    }
    """
    Then the response status should be 200
    And the response body should contain "results"
