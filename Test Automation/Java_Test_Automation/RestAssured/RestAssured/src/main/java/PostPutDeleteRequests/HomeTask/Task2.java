package PostPutDeleteRequests.HomeTask;

import io.restassured.RestAssured;
import io.restassured.builder.RequestSpecBuilder;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import static io.restassured.RestAssured.get;
import static org.hamcrest.Matchers.greaterThan;
import static org.hamcrest.Matchers.hasItem;

public class Task2 {

    @BeforeClass
    public void setUp(){
        RestAssured.baseURI="https://jsonplaceholder.typicode.com";

        RestAssured.requestSpecification=new RequestSpecBuilder().build();
    }

    @Test
    public void validateAPIResponse(){
        get("/users").then().statusCode(200)
                .body("size()", greaterThan(3))
                .body("name",hasItem("Ervin Howell"));
    }


}
