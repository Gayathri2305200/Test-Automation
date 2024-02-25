Feature: WorKing With Amazon page

  @SetLocation, @Amazon
  Scenario: Set up location
    Given user navigates to url "https://www.amazon.in/"
    When user clicks on location icon
    Then user give the pincode as "500001" and clicks on Apply button

    @BeforePrimeAction, @Amazon
  Scenario: Search for Mobiles Delivered by Tomorrow before prime action
    Given user enter the "mobile" in the search bar and clicks the search icon
    When user selects the Get It by Tomorrow checkbox
    Then user get the results status before prime setup

#      @signIn, @Amazon, @login
#  Scenario: Signing into Amazon
#    Given user clicks on  sign in
#    When user enters the MobileNum as "XXXXXXXXX" and click on continue
#    Then user enters the password as "password" and clicks the submit button


  @AfterPrimeAction, @Amazon
  Scenario: Search for Mobiles Delivered by Tomorrow after prime action
    Given user enter the "mobile" in the search bar and clicks the search icon
    When user selects the Get It by Tomorrow checkbox
    Then user get the results status after prime setup




