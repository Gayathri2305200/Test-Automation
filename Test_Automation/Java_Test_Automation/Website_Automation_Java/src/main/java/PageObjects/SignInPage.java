package PageObjects;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.WebDriverWait;

public class SignInPage {
    public static WebDriver driver;
    WebDriverWait wait;
    public SignInPage(WebDriver driver) {
        SignInPage.driver = driver;
        PageFactory.initElements(driver, this);
    }

    @FindBy(
            xpath = "//*[@id=\"nav-link-accountList\"]/span"
    )
    WebElement signinBtn;
    @FindBy(
            xpath = "//*[@id=\"ap_email\"]"
    )
    WebElement Mobilenum;
    @FindBy(
            xpath = "//*[@id=\"continue\"]"
    )
    WebElement continueBtn;
    @FindBy(
            xpath = "//*[@id=\"ap_password\"]"
    )
    WebElement txtPassword;
    @FindBy(
            xpath = "//*[@id=\"signInSubmit\"]"
    )
    WebElement SignUpBtn;


    public SignInPage SignIn() {
        this.signinBtn.click();
        return this;
    }

    public SignInPage enterNum(String MobileNum) {
        this.Mobilenum.sendKeys(new CharSequence[]{MobileNum});
        return this;
    }

    public SignInPage clickContinue() {
        this.continueBtn.click();
        return this;
    }

    public SignInPage EnterPassword(String Password) throws InterruptedException {
        this.txtPassword.sendKeys(new CharSequence[]{Password});
        return this;
    }

    public SignInPage clickSignIn() {
        this.SignUpBtn.click();
        return this;
    }

    public SearchMobile SignInpage(String MobileNum, String password) throws InterruptedException {
        this.SignIn();
        this.enterNum(MobileNum);
        this.clickContinue();
        this.EnterPassword(password);
        this.clickSignIn();
        return new SearchMobile(driver);
    }
}


