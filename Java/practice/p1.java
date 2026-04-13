import java.util.Scanner;

public class p1 {
    public static void main (String[] args) {
        Scanner vote = new Scanner(System.in);
        System.out.println("Enter your age: ");
        int age = vote. nextInt();
        if (age >= 18) {
            System.out.println("You are eligible to vote");
        } else {
            System.out.println("You are not eligible to vote");
        }
        
    }
}