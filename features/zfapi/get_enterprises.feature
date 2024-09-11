Feature: Enterprises

Scenario: Get all enterprises from ZF API
    Given the ZF API is available
    When the user retrieves all the enterprises from "1.0/enterprises"
    Then the status code should be "200"
    And the response should contain a list of enterprises

Scenario: Get specific enterprise from ZF API
    Given the ZF API is available
    When the user retrieves the enterprise "73585260" from "1.0/enterprises"
    Then the status code should be "200"


Scenario: Get the protected accounts associated with the given enterprise
    Given the ZF API is available
    When the user retrieves the protected accounts of the enterprise "73585260" from "1.0/enterprises"
    Then the status code should be "200"
    And the response should have the protected accounts associated with the enterprise
    