import java.util.Scanner;

class Student1 {
    String name;
    int marks;

    void inputDetails(Scanner sc) {
        System.out.print("Enter Student Name: ");
        name = sc.nextLine();

        System.out.print("Enter Marks: ");
        marks = sc.nextInt();
        sc.nextLine();
    }

    void displayDetails() {
        System.out.println("Name: " + name + ", Marks: " + marks);
    }
}

public class TopperFinder {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of students: ");
        int n = sc.nextInt();
        sc.nextLine();

        Student1[] students = new Student1[n];

        System.out.println("\nEnter Student Details:");

        for(int i = 0; i < n; i++) {
            students[i] = new Student1();
            System.out.println("\nStudent " + (i+1) + ":");
            students[i].inputDetails(sc);
        }

        Student1 topper = students[0];

        for(int i = 1; i < n; i++) {
            if(students[i].marks > topper.marks) {
                topper = students[i];
            }
        }

        System.out.println("\nTopper Student Details:");
        topper.displayDetails();

        sc.close();
    }
}
