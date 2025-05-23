Feature: OrangeHRM Login

  Background:
    Given I launch Chrome browser
    When I open orange hrm Homepage
    And Enter username "Admin" and password "admin123"
    And Click on login button

  Scenario: Login to OrangeHRM with valid credentials
    Then User must successfully login to the Dashboard page


  Scenario: Leave page
    When Navigate to leave page
    Then leave page should display

  Scenario: Time user
    When Navigate to Time page
    Then Time page should display


