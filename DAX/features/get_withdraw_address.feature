Feature: get withdraw address

  Scenario:  get btc withdraw address
    Given I am logged dax
    And I set "Content-Type" header to "application/json"
    When I make a GET request to "/api/v2/withdraw_address/?coin_type=BTC"
    Then the response status should be 200
    And the response body should contain "results"
