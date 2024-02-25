package parameterisation.HomeTask;

public class Employee {

    private String name;
    private String salary;
    private String age;


    public Employee(String name, String salary, String age) {
        this.name = name;
        this.salary = salary;
        this.age = age;
    }

    public Employee setName(String name) {
        this.name = name;
        return this;
    }

    public Employee setSalary(String salary) {
        this.salary = salary;
        return this;
    }

    public Employee setAge(String age) {
        this.age = age;
        return this;
    }

    public String getName() {
        return name;
    }

    public String getSalary() {
        return salary;
    }

    public String getAge() {
        return age;
    }
}

