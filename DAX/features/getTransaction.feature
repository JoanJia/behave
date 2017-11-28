Feature: getTransaction

  Scenario:  get btc deposite history
    Given I am logged dax
    And I set "Content-Type" header to "application/json"
    When I make a GET request to "/api/v2/user_transaction/?tx_type=DEPOSIT&coin_type=BTC"
    Then the response status should be 200
    And the response body should contain "results"

  Scenario:  get withdraw btc history
    Given I am logged dax
    And I set "Content-Type" header to "application/json"
    When I make a GET request to "/api/v2/user_transaction/?tx_type=WITHDRAW&coin_type=BTC"
    Then the response status should be 200
    And the response body should contain "results"
