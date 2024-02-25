package testRunner;

import io.cucumber.junit.Cucumber;
import io.cucumber.junit.CucumberOptions;
import org.junit.runner.RunWith;

@RunWith(Cucumber.class)
@CucumberOptions(
        features = "src/test/java/featureFiles/feature.feature"
        ,glue={"stepDefinitions"},
        plugin = {
                "pretty", "html:target/cucumber-reports/cucumber-pretty",
                "json:target/cucumber-reports/cucumberTestReport.json",
                "junit:target/cucumber-reports/junit_xml"
        },
        monochrome = true
        //dryRun = true
        //tags={"@SignIn","@Amazon"}  SignIn and Amazon executes
        //tags={"@SignIn,@Amazon"}  SignIn or Amazon executes
        //tags={"@Amazon"}

)
public class Runner {
}
