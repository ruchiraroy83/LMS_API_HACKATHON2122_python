Feature: To check The GET method for Skills
  
Scenario: Verify GET all Skills for Skill Master
    Given Skills User is on Endpoint: url/Skills with valid username and password
    When skills User sends GET request 
    Then skills User validates StatusCode
    And skills JSON schema is valid


Scenario Outline: Verify GET for a Skill with specific ID
    Given Skills User is on Endpoint: url/Skills with valid username and password
    When User sends GET request on skill id from "<SheetName>" and <RowNumber>
    Then skills User validates the StatusCode and StatusMessage from "<SheetName>" sheet and <RowNumber> row
    And JSON schema is valid for "<Method>" in Skills
    And skills check the Database
    Examples:
        | SheetName  | RowNumber | Method |
        | Skills_GET | 0         | GET    |