package RestAssuredIntroduction.HomeTask1;

import org.testng.Assert;
import org.testng.annotations.Test;
import restAssuredIntroduction.HomeTask1.Task1;


public class Task1_Test extends Task1 {
    @Test
    public void verifyNoOfResourcesInPosts(){
        Assert.assertEquals(getNoOfResourcesInPosts(),100);
    }
    @Test
    public void verifyNoOfResourcesInComments(){
        Assert.assertEquals(getNoOfResourcesInComments(),500);
    }
    @Test
    public void verifyNoOfResourcesInAlbums(){
        Assert.assertEquals(getNoOfResourcesInAlbums(),100);
    }
    @Test
    public void verifyNoOfResourcesInPhotos(){
        Assert.assertEquals(getNoOfResourcesInPhotos(),5000);
    }
    @Test
    public void verifyNoOfResourcesInTodos() {
        Assert.assertEquals(getNoOfResourcesInTodos(), 200);
    }
    @Test
    public void verifyNoOfResourcesInUsers() {
        Assert.assertEquals(getNoOfResourcesInUsers(), 10);
    }

}
