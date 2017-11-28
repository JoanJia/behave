Feature: Withdraw request

  Scenario: cancel  all the open withdraw requests
    Given I am logged dax
    And I send get withdraw history request
    Then I cancel all the requests which "id" in the history list


  Scenario: cancel canceled withdraw requests
    Given I am logged dax
    And I set "Content-Type" header to "application/json"
    When I make a POST request to "/api/v2/withdraw/53/cancel/"
    Then the response status should be 500
    And the response body should contain "detail"


  Scenario: Get Withdraw history status
    Given I am logged dax
    And I set "Content-Type" header to "application/json"
    When I make a GET request to "/api/v2/withdraw/"
    Then the response status should be 200
    Then the response body should contain "status"


  Scenario: Send Withdraw request and cancel it
    Given I am logged dax
    And I set "Content-Type" header to "application/json"
    When I make a POST request to "/api/v2/withdraw/"
    """
      {
       "tx_amount": 0.001,
       "coin_type": "btc",
       "address":"mmA4ND54mYy73G3eAifHLNxB2z4YKeDu2J"
       }
    """
    Then the response status should be one of "201,400"
    And the response body should contain one of "status,non_field_errors"
    When I store the JSON at path "id" in "id"
    Then I cancel the withdraw request with id
    Then the response status should be 200







