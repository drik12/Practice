import java.util.Scanner;

class Employee {
    int id;
    String name;
    double salary;

    // Method to display employee details
    void display() {
        System.out.println("\nEmployee Details");
        System.out.println("Employee ID: " + id);
        System.out.println("Employee Name: " + name);
        System.out.println("Employee Salary: " + salary);
    }
}

public class EmployeeDetails {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Create object of Employee class
        Employee emp = new Employee();

        // Input values using Scanner
        System.out.print("Enter Employee ID: ");
        emp.id = sc.nextInt();

        sc.nextLine(); // consume newline

        System.out.print("Enter Employee Name: ");
        emp.name = sc.nextLine();

        System.out.print("Enter Employee Salary: ");
        emp.salary = sc.nextDouble();

        // Call display method
        emp.display();

        sc.close();
    }
}