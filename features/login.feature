Feature: OrangeHRM Login
  Scenario: Login to OrangeHRM with valid credentials
    Given I launch Chrome browser
    When I open orange hrm Homepage
    And Enter username "Admin" and password "admin123"
    And Click on login button
    Then User must successfully login to the Dashboard page