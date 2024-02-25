package StepDefinitions;

import Base.TestBase;
import com.epam.reportportal.service.ReportPortal;
import io.cucumber.java.AfterAll;
import io.cucumber.java.AfterStep;
import io.cucumber.java.Before;
import io.cucumber.java.BeforeAll;
import io.cucumber.java.Scenario;
import org.apache.commons.io.FileUtils;
import org.apache.logging.log4j.LogManager;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;

import java.io.File;
import java.io.IOException;
import java.util.Calendar;
import java.util.logging.Logger;

public class ServiceHooks {
    static TestBase baseTest;
    static WebDriver  driver;
    //Logger logger= LogManager.getLogger(ServiceHooks.class);

    @Before
    public static void initializeBrowser() {
        baseTest = new TestBase();
        driver = baseTest.openBrowser("edge");
    }

    @AfterStep
    public void captureScreenshot(Scenario scenario) throws IOException {
        File screenshot = ((TakesScreenshot) baseTest.driver).getScreenshotAs(OutputType.FILE);
        FileUtils.copyFileToDirectory(screenshot, new File(System.getProperty("user.dir") + "screenshots"));
        ReportPortal.emitLog("this a screenshot for scenario ---> " + scenario.getName(), "INFO", Calendar.getInstance().getTime(), screenshot);
    }

    @AfterAll
    public static void tearDown() {

    }
}
