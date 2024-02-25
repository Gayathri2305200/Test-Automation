package pageObjects;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class HomePage {
    public  static WebDriver driver;
    public HomePage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }


    @FindBy(xpath="//*[@id=\"glow-ingress-line2\"]")
    WebElement SelectPincode;

    @FindBy(xpath="//div[2]/div/div[1]/input")
    WebElement givepincode;

    @FindBy(xpath="//*[@id=\"GLUXZipUpdate\"]/span/input")
    WebElement apply_btn;


    public HomePage SelectAddressCode()
    {
        SelectPincode.click();
        return this;
    }
    public HomePage SendPincode(String pincode) throws InterruptedException {
        Thread.sleep(1000);
        givepincode.sendKeys(pincode);
        return this;
    }

    public void ClickOnApply() throws InterruptedException {
        Thread.sleep(1000);
        apply_btn.click();
        Thread.sleep(1000);}
    public void GoTOSearchNMobilePage(String pincode) throws InterruptedException {
        SelectAddressCode();
        SendPincode(pincode);
        ClickOnApply();
    }
}
