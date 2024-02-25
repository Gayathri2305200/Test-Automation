package parameterisation.HomeTask;

import io.restassured.RestAssured;
import io.restassured.builder.RequestSpecBuilder;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import static io.restassured.RestAssured.delete;
import static io.restassured.RestAssured.get;
import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;

public class PractiseTask {
    @BeforeClass
    public void setUp(){
        RestAssured.baseURI="https://dummy.restapiexample.com/api";
        RestAssured.basePath="/v1";

        RestAssured.requestSpecification=new RequestSpecBuilder()
                .build();
    }


    @Test
    public void getEmployees() {
        Employee employee;

        int count =get("/employees").jsonPath().getInt("data.size()");
        System.out.println(count);

        // Get the list of all employees.
        get("/employees").then().statusCode(200).
                statusLine("HTTP/1.1 200 OK").
                contentType("application/json").
                // body("Content-Encoding",equalTo("gzip")).
                        body("data.size()",equalTo(count)).log().all();


        employee=new Employee("Gayathri","5678","22");

        // create a new employee and verify whether employee is added or not
        given().body(employee).post("/create").then().body("message",equalTo("Successfully! Record has been added."));

        //  verify the count of employees is increased by +1
        get("/employees").
                then().assertThat().body("data.size()",equalTo(count+1));

        //get the details of the employee created in step 2
        get("/employee/25").then().body("name",equalTo("Gayathri"))
                .body("salary",equalTo(5678))
                .body("age",equalTo(22));

        //update the details of the employee update the salary and age
        employee.setSalary("7896");
        employee.setAge("25");
        given().body(employee).
                when().get("/employee/25").
                then().body("message",equalTo("Successfully! Records has been updated."));

        //get the details of the employee created in step 2
        get("/employee/25").then()
                .body("salary",equalTo(7896)).body("age",equalTo("25"));

        //delete the employee created in step 2.
        delete("/employee/25").then()
                .body("message",equalTo("Successfully! Records has been deleted."))
                .body("data.size()",equalTo(count-1));
    }

}
