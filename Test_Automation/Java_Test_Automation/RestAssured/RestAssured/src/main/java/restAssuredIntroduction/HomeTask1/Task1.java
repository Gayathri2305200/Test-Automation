package restAssuredIntroduction.HomeTask1;

import io.restassured.RestAssured;
import io.restassured.response.Response;



public class Task1 {
    public int getNoOfResourcesInPosts() {
        Response response =RestAssured.get("https://jsonplaceholder.typicode.com/posts");
        int noOfResources = response.jsonPath().getList("$").size();
        return noOfResources;
    }
    public int getNoOfResourcesInComments() {
        Response response =RestAssured.get("https://jsonplaceholder.typicode.com/comments");
        int noOfResources = response.jsonPath().getList("$").size();
        return noOfResources;
    }
    public int getNoOfResourcesInAlbums() {
        Response response =RestAssured.get("https://jsonplaceholder.typicode.com/albums");
        int noOfResources = response.jsonPath().getList("$").size();
        return noOfResources;
    }
    public int getNoOfResourcesInPhotos() {
        Response response =RestAssured.get("https://jsonplaceholder.typicode.com/photos");
        int noOfResources = response.jsonPath().getList("$").size();
        return noOfResources;
    }
    public int getNoOfResourcesInTodos() {
        Response response =RestAssured.get("https://jsonplaceholder.typicode.com/todos");
        int noOfResources = response.jsonPath().getList("$").size();
        return noOfResources;
    }
    public int getNoOfResourcesInUsers() {
        Response response =RestAssured.get("https://jsonplaceholder.typicode.com/users");
        int noOfResources = response.jsonPath().getList("$").size();
        return noOfResources;
    }
}
