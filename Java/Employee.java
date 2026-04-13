class Employee {
    String name;
    double salary;

    //Constructor 1: only name
    Employee(String n) {
        name = n;
        salary = 0.0;
    }

    //Constructor 2: name and salary
    Employee(String n, double s) {
        name = n;
        salary = s;
    }

    //Method to display details
    void display() {
        System.out.println("Name: " + name);
        System.out.println("Salary: " + salary);
    }

    public static void main(String[] args) {
        //Employee created with only name
        Employee e1 = new Employee("Rahul");
        //Employee created with name and salary
        Employee e2 = new Employee("Anita", 50000);

        e1.display();
        e2.display();
    }
}
