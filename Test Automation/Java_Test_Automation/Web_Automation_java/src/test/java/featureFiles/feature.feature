Feature: WorKing With Amazon page

  @SetLocation, @Amazon
  Scenario: Set up location
    Given user navigates to url "https://www.amazon.in/"
    When user clicks on location icon
    Then user give the pincode as "500001" and clicks on Apply button
