package stepDefinitions;

import base.BaseTest;
import com.epam.reportportal.service.ReportPortal;
import io.cucumber.java.AfterAll;
import io.cucumber.java.AfterStep;
import io.cucumber.java.BeforeAll;
import io.cucumber.java.Scenario;
import org.apache.commons.io.FileUtils;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;

import java.io.File;
import java.io.IOException;
import java.util.Calendar;
import java.util.logging.Logger;


public class ServiceHooks {

        //static BaseTest baseTest= new BaseTest();
    static WebDriver driver;
        //Logger logger= LogManager.getLogger(ServiceHooks.class);

        @BeforeAll
        public static void initializeBrowser() {
            driver=BaseTest.openBrowser("edge");
        }

//        @AfterStep
//        public void captureScreenshot(Scenario scenario) throws IOException {
//            File screenshot = ((TakesScreenshot) driver).getScreenshotAs(OutputType.FILE);
//            FileUtils.copyFileToDirectory(screenshot, new File(System.getProperty("user.dir") + "src/main/resources/screenshots"));
//            ReportPortal.emitLog("this a screenshot for scenario ---> " + scenario.getName(), "INFO", Calendar.getInstance().getTime(), screenshot);
//        }

        @AfterAll
        public static void tearDown() {
            driver.quit();
        }
    }


