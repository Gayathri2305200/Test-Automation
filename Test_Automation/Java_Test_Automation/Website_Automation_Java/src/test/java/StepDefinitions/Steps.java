package StepDefinitions;

import Base.TestBase;
import PageObjects.HomePage;
import PageObjects.SearchMobile;
import PageObjects.SignInPage;
import io.cucumber.java.en.*;

public class Steps extends TestBase {
    HomePage hp;
    SearchMobile sm;
    SignInPage sp;
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

    @Given("user enter the {string} in the search bar and clicks the search icon")
    public void user_enter_the_in_the_search_bar_and_clicks_the_search_icon(String text) {
        sm=new SearchMobile(driver);
        sm.SendText(text);
        sm.clickOnSearch();
    }

    @When("user selects the Get It by Tomorrow checkbox")
    public void user_selects_the_get_it_by_tomorrow_checkbox() throws InterruptedException {
       sm.clickOnGetItByTomorrow();
    }

    @Then("user get the results status before prime setup")
    public void user_get_the_results_status_before_prime_setup() throws InterruptedException {
        sm.ResultBeforePrime();
    }

    @Given("user clicks on  sign in")
    public void user_clicks_on_sign_in() {
        sp=new SignInPage(driver);
        sp.SignIn();
    }

    @When("user enters the MobileNum as {string} and click on continue")
    public void user_enters_the_mobile_num_as_click_continue(String MobileNum) {
     sp.enterNum(MobileNum);
     sp.clickContinue();
    }

    @Then("user enters the password as {string} and clicks the submit button")
    public void user_enters_the_password_as_and_clicks_the_submit_button(String password) throws InterruptedException {
        sp.EnterPassword(password);
        sp.clickSignIn();
    }

    @Then("user get the results status after prime setup")
    public void user_get_the_results_status_after_prime_setup() throws InterruptedException {
       sm.ResultafterPrime();
    }


}
