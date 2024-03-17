package stepDefinitions;

import base.BaseTest;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import pageObjects.HomePage;

public class Steps extends BaseTest {
    HomePage hp;

    @Given("user navigates to url {string}")
    public void user_navigates_to_url(String url) {
        driver.get(url);
    }

    @When("user clicks on location icon")
    public void user_clicks_on_location_icon() {
        hp=new HomePage(driver);
        hp.SelectAddressCode();
    }

    @Then("user give the pincode as {string} and clicks on Apply button")
    public void user_give_the_pincode_as_and_clicks_on_apply_button(String pincode) throws InterruptedException {
        hp.SendPincode(pincode);
        hp.ClickOnApply();
    }
}
