import java.util.Scanner;

public class AS2_CollatzSequence {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a positive integer: ");
        int n = sc.nextInt();

        if (n <= 0) {
            System.out.println("Please enter a positive integer.");
            return;
        }

        System.out.print("Collatz sequence: ");

        while (n != 1) {
            System.out.print(n + " ");

            if (n % 2 == 0) {
                n = n / 2;        // If even
            } else {
                n = 3 * n + 1;    // If odd
            }
        }

        System.out.println(1);
        sc.close();
    }
}