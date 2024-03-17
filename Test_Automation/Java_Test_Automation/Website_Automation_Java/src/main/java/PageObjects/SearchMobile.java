package PageObjects;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class SearchMobile {
        public static WebDriver driver;
        public SearchMobile(WebDriver driver) {
            this.driver = driver;
            PageFactory.initElements(driver, this);
        }
    @FindBy(xpath = "//input[@id='twotabsearchtextbox']")
    WebElement search_bar;
    @FindBy(xpath="//input[@id='nav-search-submit-button']")
    WebElement search_icon;
        @FindBy(xpath = "//*[@id=\"p_90/6741118031\"]/span/a/div/label/i")
        WebElement GetItByTomorrow;


        public SearchMobile SendText(String text) {
            this.search_bar.click();
            this.search_bar.clear();
            this.search_bar.sendKeys(text);
            return this;
        }

        public SearchMobile clickOnSearch() {
            this.search_icon.click();
            return this;
        }

        public SearchMobile clickOnGetItByTomorrow() throws InterruptedException {
            Thread.sleep(1000L);
            this.GetItByTomorrow.click();
            Thread.sleep(1000L);
            return this;
        }

        public void ResultBeforePrime() throws InterruptedException {
            WebElement results = driver.findElement(By.xpath("//*[@id=\"search\"]//h1//div[1]/div/div/span[1]"));
            String[] results_string = results.getText().split(" ");
            System.out.println("The results before prime action are: " + results_string[2]);
        }

        public void ResultafterPrime() throws InterruptedException {
            Thread.sleep(1000L);
            WebElement results = driver.findElement(By.xpath("//*[@id=\"search\"]/span/div/h1/div/div[1]/div/div/span[1]"));
            String[] results_string = results.getText().split(" ");
            System.out.println("The results after prime action are: " + results_string[2]);
        }

        public SignInPage setSearchMobile(String text) throws InterruptedException {
            SendText(text);
            clickOnSearch();
            clickOnGetItByTomorrow();
            ResultBeforePrime();
            ResultafterPrime();
            return new SignInPage(driver);
        }
}
