package restAssuredIntroduction.HomeTask1;

import io.restassured.RestAssured;
import io.restassured.response.Response;
import org.testng.annotations.Test;

public class Task2 {

    public int getResponseCodeInPosts(){

//        RestAssured.given().baseUri("https://jsonplaceholder.typicode.com")
//                .when().get("/posts/1")
//                .then().assertThat().statusCode(200)
//                .body("userId",equalTo(1))
//                .body("title",equalTo("sunt aut facere repellat provident occaecati excepturi optio reprehenderit"))
//                .body("body",equalTo("quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"));

        Response response =RestAssured.given().baseUri("https://jsonplaceholder.typicode.com")
                .when().get("/posts/96");
        int statusCode=response.statusCode();
        return statusCode;
    }
    public String getResponseBodyInPosts(){
        Response response =RestAssured.given().baseUri("https://jsonplaceholder.typicode.com")
                .when().get("/posts/96");
        String responseBody=response.getBody().asString();
        System.out.println(responseBody);
        return responseBody;
    }


    public int getResponseCodeInComments(){
        Response response =RestAssured.given().baseUri("https://jsonplaceholder.typicode.com")
                .when().get("/comments/2");
        int statusCode=response.statusCode();
        return statusCode;
    }
    @Test
    public String getResponseBodyInComments(){
        Response response =RestAssured.given().baseUri("https://jsonplaceholder.typicode.com")
                .when().get("/comments/2");
        String responseBody=response.getBody().asString();
        System.out.println(responseBody);
        return responseBody;
    }
    public int getResponseCodeInAlbums(){
        Response response =RestAssured.given().baseUri("https://jsonplaceholder.typicode.com")
                .when().get("/albums/2");
        int statusCode=response.statusCode();
        return statusCode;
    }
    @Test
    public String getResponseBodyInAlbums(){
        Response response =RestAssured.given().baseUri("https://jsonplaceholder.typicode.com")
                .when().get("/albums/2");
        String responseBody=response.getBody().asString();
        System.out.println(responseBody);
        return responseBody;
    }
    public int getResponseCodeInPhotos(){
        Response response =RestAssured.given().baseUri("https://jsonplaceholder.typicode.com")
                .when().get("/photos/8");
        int statusCode=response.statusCode();
        return statusCode;
    }
    public String getResponseBodyInPhotos(){
        Response response =RestAssured.given().baseUri("https://jsonplaceholder.typicode.com")
                .when().get("/photos/8");
        String responseBody=response.getBody().asString();
        System.out.println(responseBody);
        return responseBody;
    }
    public int getResponseCodeInTodos(){
        Response response =RestAssured.given().baseUri("https://jsonplaceholder.typicode.com")
                .when().get("/todos/3");
        int statusCode=response.statusCode();
        return statusCode;
    }
    public String getResponseBodyInTodos(){
        Response response =RestAssured.given().baseUri("https://jsonplaceholder.typicode.com")
                .when().get("/todos/3");
        String responseBody=response.getBody().asString();
        System.out.println(responseBody);
        return responseBody;
    }
    public int getResponseCodeInUsers(){
        Response response =RestAssured.given().baseUri("https://jsonplaceholder.typicode.com")
                .when().get("/users/6");
        int statusCode=response.statusCode();
        return statusCode;
    }

    public String getResponseBodyInUsers(){
        Response response =RestAssured.given().baseUri("https://jsonplaceholder.typicode.com")
                .when().get("/users/6");
        String responseBody=response.getBody().asString();
        System.out.println(responseBody);
        return responseBody;
    }
}
