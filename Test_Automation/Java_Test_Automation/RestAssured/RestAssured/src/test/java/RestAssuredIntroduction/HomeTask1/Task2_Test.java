package RestAssuredIntroduction.HomeTask1;

import org.testng.Assert;
import org.testng.annotations.Test;
import restAssuredIntroduction.HomeTask1.Task2;

public class Task2_Test extends Task2 {
    @Test
    public void verifyResponseCodeAndBodyInPosts() {
        String responseBody ="{\n" +
                "  \"userId\": 10,\n" +
                "  \"id\": 96,\n" +
                "  \"title\": \"quaerat velit veniam amet cupiditate aut numquam ut sequi\",\n" +
                "  \"body\": \"in non odio excepturi sint eum\\nlabore voluptates vitae quia qui et\\ninventore itaque rerum\\nveniam non exercitationem delectus aut\"\n" +
                "}";
        Assert.assertEquals(getResponseBodyInPosts(), responseBody);
        Assert.assertEquals(getResponseCodeInPosts(), 200);
    }

    @Test
    public void verifyResponseCodeAndBodyInComments() {
        String responseBody = "{\n" +
                "  \"postId\": 1,\n" +
                "  \"id\": 2,\n" +
                "  \"name\": \"quo vero reiciendis velit similique earum\",\n" +
                "  \"email\": \"Jayne_Kuhic@sydney.com\",\n" +
                "  \"body\": \"est natus enim nihil est dolore omnis voluptatem numquam\\net omnis occaecati quod ullam at\\nvoluptatem error expedita pariatur\\nnihil sint nostrum voluptatem reiciendis et\"\n" +
                "}";
        Assert.assertEquals(getResponseBodyInComments(), responseBody);
        Assert.assertEquals(getResponseCodeInComments(), 200);
    }
    @Test
    public void verifyResponseCodeAndBodyInAlbums() {
        String responseBody = "{\n" +
                "  \"userId\": 1,\n" +
                "  \"id\": 2,\n" +
                "  \"title\": \"sunt qui excepturi placeat culpa\"\n" +
                "}";
        Assert.assertEquals(getResponseBodyInAlbums(), responseBody);
        Assert.assertEquals(getResponseCodeInAlbums(), 200);
    }
    @Test
    public void verifyResponseCodeAndBodyInPhotos() {
        String responseBody = "{\n" +
                "  \"albumId\": 1,\n" +
                "  \"id\": 8,\n" +
                "  \"title\": \"aut porro officiis laborum odit ea laudantium corporis\",\n" +
                "  \"url\": \"https://via.placeholder.com/600/54176f\",\n" +
                "  \"thumbnailUrl\": \"https://via.placeholder.com/150/54176f\"\n" +
                "}";
        Assert.assertEquals(getResponseBodyInPhotos(), responseBody);
        Assert.assertEquals(getResponseCodeInPhotos(), 200);
    }@Test
    public void verifyResponseCodeAndBodyInTodos() {
        String responseBody = "{\n" +
                "  \"userId\": 1,\n" +
                "  \"id\": 3,\n" +
                "  \"title\": \"fugiat veniam minus\",\n" +
                "  \"completed\": false\n" +
                "}";
        Assert.assertEquals(getResponseBodyInTodos(), responseBody);
        Assert.assertEquals(getResponseCodeInTodos(), 200);
    }@Test
    public void verifyResponseCodeAndBodyInUsers() {
        String responseBody = "{\n" +
                "  \"id\": 6,\n" +
                "  \"name\": \"Mrs. Dennis Schulist\",\n" +
                "  \"username\": \"Leopoldo_Corkery\",\n" +
                "  \"email\": \"Karley_Dach@jasper.info\",\n" +
                "  \"address\": {\n" +
                "    \"street\": \"Norberto Crossing\",\n" +
                "    \"suite\": \"Apt. 950\",\n" +
                "    \"city\": \"South Christy\",\n" +
                "    \"zipcode\": \"23505-1337\",\n" +
                "    \"geo\": {\n" +
                "      \"lat\": \"-71.4197\",\n" +
                "      \"lng\": \"71.7478\"\n" +
                "    }\n" +
                "  },\n" +
                "  \"phone\": \"1-477-935-8478 x6430\",\n" +
                "  \"website\": \"ola.org\",\n" +
                "  \"company\": {\n" +
                "    \"name\": \"Considine-Lockman\",\n" +
                "    \"catchPhrase\": \"Synchronised bottom-line interface\",\n" +
                "    \"bs\": \"e-enable innovative applications\"\n" +
                "  }\n" +
                "}";
        Assert.assertEquals(getResponseBodyInUsers(), responseBody);
        Assert.assertEquals(getResponseCodeInUsers(), 200);

    }



}
