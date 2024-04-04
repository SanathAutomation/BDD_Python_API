Feature: Verify countries and perform CRUD operations
  As a user
  I will send GET requests
  I want to be able to see the expected response


  Scenario: GET country names happy path
    Given I set the GET endpoint for fetching country names
    When I send GET HTTP request
    Then I expect the HTTP response code of "GET" to be "200" and get country names



  Scenario: GET currency status code and message which does not exist for Unhappy path
    Given I set the GET endpoint for fetching country names which does not exist
    When I send a GET HTTP request
    Then I expect the HTTP response code of "GET" to be "404" and did not get the country names



