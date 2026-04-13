import java.util.Scanner;

// Parent class
class Employee {

    String name;
    int employeeId;
    double salary;

    // Method to take employee details
    void inputEmployeeDetails(Scanner sc) {

        System.out.print("Enter Employee Name: ");
        name = sc.nextLine();

        System.out.print("Enter Employee ID: ");
        employeeId = sc.nextInt();

        System.out.print("Enter Salary: ");
        salary = sc.nextDouble();

        sc.nextLine(); // consume newline
    }

    // Method to display employee details
    void displayEmployeeDetails() {
        System.out.println("\nEmployee Details");
        System.out.println("Name: " + name);
        System.out.println("Employee ID: " + employeeId);
        System.out.println("Salary: " + salary);
    }
}

// Child class
class Manager extends Employee {

    String department;
    int teamSize;

    // Method to take manager details
    void inputManagerDetails(Scanner sc) {

        System.out.print("Enter Department: ");
        department = sc.nextLine();

        System.out.print("Enter Team Size: ");
        teamSize = sc.nextInt();
    }

    // Method to display manager details
    void displayManagerDetails() {

        // Display inherited employee details
        displayEmployeeDetails();

        // Display extra manager details
        System.out.println("\nManager Additional Details");
        System.out.println("Department: " + department);
        System.out.println("Team Size: " + teamSize);
    }
}

// Main class
public class Organization {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Create Manager object
        Manager m1 = new Manager();

        // Input employee + manager details
        m1.inputEmployeeDetails(sc);
        m1.inputManagerDetails(sc);

        // Display all details
        m1.displayManagerDetails();

        sc.close();
    }
}
