Feature: FYI submit a request page tests
  This tests are designed for the submit a request page in the FYI web app

@Test-03
Scenario: Contact Support Button Redirects User to the Submit Request Page
  Given The user is on home page
  When  The user displays the hamburger menu
  And   The user clicks the "Help" option on the menu
  And   The user click the contact support button on the help page
  Then  The user can see the submit a request page

@Test-04
Scenario: Verify Search Results for AI on the Submit a Request Page
  Given The user is on the submit a request page
  When  The user search "AI" on the search field
  Then  The user should received "15" articles