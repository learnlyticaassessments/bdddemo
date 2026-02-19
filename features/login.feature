Feature: Login

  Scenario: Successful login
    Given the user is on the login page
    When the user logs in with username "standard_user" and password "secret_sauce"
    Then the dashboard should be visible
