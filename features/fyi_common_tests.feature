Feature: FYI common tests
  This tests are designed for the FYI web app common section

Background:
  Given The user is on home page
  When  The user displays the hamburger menu

@Test-01
Scenario: Terms of Service Page Displays the correct copyright at the Bottom
  And   The user clicks the "Terms of Service" option on the menu
  Then  The user can see "©2024 FYI.FYI, Inc." copyright on the page footer

@Test-02
Scenario: Hamburger Menu Contains Correct User Selection Options
  Then  The user validates if the options "Home, Help, About Us, The Team, Press, Terms of Service, Privacy Policy" are the displayed on the hamburger menu
