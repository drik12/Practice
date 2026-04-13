// Parent class
class Person {
    String name;
    int age;

    // Method to set person details
    void setPersonDetails(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Method to display person details
    void displayPersonDetails() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }
}

// Child class inheriting Person
class Student extends Person {
    int studentId;
    String course;

    // Method to set student details
    void setStudentDetails(int studentId, String course) {
        this.studentId = studentId;
        this.course = course;
    }

    // Method to display student details
    void displayStudentDetails() {
        // Inherited method from Person
        displayPersonDetails();

        // Student-specific details
        System.out.println("Student ID: " + studentId);
        System.out.println("Course: " + course);
    }
}

// Main class
public class Inheritance {
    public static void main(String[] args) {

        // Create Student object
        Student s1 = new Student();

        // Set inherited Person details
        s1.setPersonDetails("Diganta", 20);

        // Set Student details
        s1.setStudentDetails(25067, "Artificial Intelligence & Science");

        // Display all details
        System.out.println("Student Information:");
        s1.displayStudentDetails();
    }
}
