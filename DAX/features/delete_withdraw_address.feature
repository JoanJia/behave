Feature: Delete

  Scenario:  get btc deposite history
    Given I am logged dax
    And I set "Content-Type" header to "application/json"
    When I get withdraw history
    Then delete all the address which "id" in the history list
    When I create a withdraw address
#    And I save the
    When I make a DELETE request to "/api/v2/withdraw_address/90"
    Then the response status should be 204
