import java.util.Scanner;

class Student {
    int mark1, mark2, mark3;
    int total;
    double average;

    // Method to calculate total marks
    void calculateTotal() {
        total = mark1 + mark2 + mark3;
    }

    // Method to calculate average marks
    void calculateAverage() {
        average = total / 3.0;
    }

    // Method to display results
    void display() {
        System.out.println("\nStudent Result");
        System.out.println("Total Marks = " + total);
        System.out.println("Average Marks = " + average);
    }
}

public class StudentMarksDemo {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Create object of Student class
        Student s = new Student();

        // Input marks
        System.out.print("Enter marks of Subject 1: ");
        s.mark1 = sc.nextInt();

        System.out.print("Enter marks of Subject 2: ");
        s.mark2 = sc.nextInt();

        System.out.print("Enter marks of Subject 3: ");
        s.mark3 = sc.nextInt();

        // Call methods
        s.calculateTotal();
        s.calculateAverage();
        s.display();

        sc.close();
    }
}
