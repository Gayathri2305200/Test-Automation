package dataDrivenTesting;

import io.restassured.RestAssured;
import io.restassured.builder.RequestSpecBuilder;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.equalToIgnoringCase;
import static org.hamcrest.Matchers.greaterThan;

public class Task2 {

    @BeforeClass
    public void setUp(){
        RestAssured.baseURI="http://api.openweathermap.org";
        RestAssured.basePath="/data/2.5/weather";

        RestAssured.requestSpecification=new RequestSpecBuilder()
                .build();
    }

    @Test
    public void getWeatherDetails(){
        given().queryParam("q","hyderabad").queryParam("appid","547ee1495b18999b528ff3fd1b3faf0f")
                .when().get().then().log().all();
    }

    @Test
    public void verifyWeatherDetails(){
        given().queryParam("lat",17.3753)
                .queryParam("lon",78.4744)
                .queryParam("appid","547ee1495b18999b528ff3fd1b3faf0f")
                .when().get()
                .then().body("name",equalToIgnoringCase("hyderabad"))
                .body("sys.country",equalTo("IN"))
                .body("main.temp_min",greaterThan(0f))
                .body("main.temp",greaterThan(0f));
    }
}
