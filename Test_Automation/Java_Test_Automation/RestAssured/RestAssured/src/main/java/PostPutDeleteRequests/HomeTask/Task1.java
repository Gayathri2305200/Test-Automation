package PostPutDeleteRequests.HomeTask;

import io.restassured.RestAssured;
import io.restassured.builder.RequestSpecBuilder;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import static io.restassured.RestAssured.get;
import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;

public class Task1 {

    @BeforeClass
    public void setUp(){
        RestAssured.baseURI="https://petstore.swagger.io/";
        RestAssured.basePath="/v2";

        RestAssured.requestSpecification=new RequestSpecBuilder().setContentType("application/json").build();
    }

    @Test
    public void createPet(){
        String requestBody= "{\n" +
                "  \"id\": 12345,\n" +
                "  \"category\": {\n" +
                "    \"id\": 1,\n" +
                "    \"name\": \"dog\"\n" +
                "  },\n" +
                "  \"name\": \"snoopie\",\n" +
                "  \"photoUrls\": [\n" +
                "    \"string\"\n" +
                "  ],\n" +
                "  \"tags\": [\n" +
                "    {\n" +
                "      \"id\": 0,\n" +
                "      \"name\": \"string\"\n" +
                "    }\n" +
                "  ],\n" +
                "  \"status\": \"pending\"\n" +
                "}";
        given().body(requestBody).post("/pet");
    }

    @Test
    public void getPetAndValidateResponse(){
        get("/pet/12345").
               then().
                      statusCode(200).
                      contentType("application/json").
                      body("category.name",equalTo("dog")).
                      body("name",equalTo("snoopie")).
                      body("status",equalTo("pending"));
    }
}
