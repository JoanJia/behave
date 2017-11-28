Feature: Authorization

  Scenario: get jwt
    Given I am using server "$SERVER"
    Given I set  "authorization" in header
    When I make a POST request to "/api.php/account/authenticate/"
    Then I create the jwt and store it in "jwt"
    Then I set "json-web-token" header to "jwt"
    Then the response status should be 200

  Scenario:  Login and get Authorization header
    Given  I am Logged in
    Given I am using server "$DAX"
    When I send a  POST request to "/login/"
    Then the response status should be 200
    And the response body should contain "key"
    And the response body should contain "msg"
    When I store the JSON at path "key" in "key"
    And I store the JSON at path "user_info.username" in "username"
    Then I create the AccessToken and store it in "token"
    And I set "Authorization" header to "token"




