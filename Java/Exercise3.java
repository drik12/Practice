import java.util.Scanner;

public class Exercise3 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the bill amount: ");
        int billAmount = sc.nextInt();

        if (billAmount > 1000) {
            System.out.println("Discount is applicable");
        } else {
            System.out.println("Discount is not applicable");
        }

        sc.close();
    }
}