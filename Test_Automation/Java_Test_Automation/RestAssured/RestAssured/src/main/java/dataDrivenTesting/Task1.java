package dataDrivenTesting;

import io.restassured.RestAssured;
import io.restassured.builder.RequestSpecBuilder;
import io.restassured.response.Response;
import org.testng.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import java.util.List;

import static io.restassured.RestAssured.get;

public class Task1 {
    @BeforeClass
    public void setUp(){
        RestAssured.baseURI="https://wearecommunity.io/api";
        RestAssured.basePath="/v2";

        RestAssured.requestSpecification=new RequestSpecBuilder()
                .build();
    }

    @Test
    public void verifyEvents(){
        Response response=get("/events");
        List<String> namesOfEvent=response.path("events.findAll{it.language=='En'}.title");
        System.out.println(namesOfEvent.size());
        Assert.assertEquals(namesOfEvent.size(),14);

//        Assert.assertEquals(namesOfEvent.get(1),"Plastic Free July in Türkiye 2023");
//        Assert.assertEquals(namesOfEvent.get(0),"Műanyagmentes Július 2023");

    }
}
