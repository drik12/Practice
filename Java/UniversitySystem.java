import java.util.Scanner;

// Level 1: Base class
class Person {

    String name;
    int age;

    void inputPersonDetails(Scanner sc) {

        System.out.print("Enter Name: ");
        name = sc.nextLine();

        System.out.print("Enter Age: ");
        age = sc.nextInt();

        sc.nextLine(); // consume newline
    }

    void displayPersonDetails() {

        System.out.println("\nPerson Details");
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }
}

// Level 2: Derived class
class Student extends Person {

    int studentId;
    String course;

    void inputStudentDetails(Scanner sc) {

        System.out.print("Enter Student ID: ");
        studentId = sc.nextInt();

        sc.nextLine(); // consume newline

        System.out.print("Enter Course: ");
        course = sc.nextLine();
    }

    void displayStudentDetails() {

        displayPersonDetails();

        System.out.println("\nStudent Details");
        System.out.println("Student ID: " + studentId);
        System.out.println("Course: " + course);
    }
}

// Level 3: Derived class
class ResearchStudent extends Student {

    String researchTopic;
    String guideName;

    void inputResearchDetails(Scanner sc) {

        System.out.print("Enter Research Topic: ");
        researchTopic = sc.nextLine();

        System.out.print("Enter Guide Name: ");
        guideName = sc.nextLine();
    }

    void displayResearchStudentDetails() {

        displayStudentDetails();

        System.out.println("\nResearch Student Details");
        System.out.println("Research Topic: " + researchTopic);
        System.out.println("Guide Name: " + guideName);
    }
}

// Main class
public class UniversitySystem {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Create ResearchStudent object
        ResearchStudent r1 = new ResearchStudent();

        // Input all details step by step
        r1.inputPersonDetails(sc);
        r1.inputStudentDetails(sc);
        r1.inputResearchDetails(sc);

        // Display full information
        System.out.println("\nFull Details");
        r1.displayResearchStudentDetails();

        sc.close();
    }
}
