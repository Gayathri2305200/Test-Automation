package dataDrivenTesting;

import io.restassured.RestAssured;
import io.restassured.http.Method;
import io.restassured.response.Response;
import io.restassured.specification.RequestSpecification;
import org.testng.Assert;

public class prac {
    public static void main(String[] args) {

//Creating BaseURI
            RestAssured.baseURI = "https://petstore.swagger.io/";
//Creating an Request
            RequestSpecification httpRequest = RestAssured.given();
//Getting an Response
            Response response = httpRequest.request(Method.GET, "v2/pet/12345");

            System.out.println(response.asPrettyString());

            System.out.println(response.getStatusLine());

            System.out.println(response.getContentType());

            System.out.println(response.getStatusCode());

            int code = response.getStatusCode();

            Assert.assertEquals(code, 200);

        }
    }
