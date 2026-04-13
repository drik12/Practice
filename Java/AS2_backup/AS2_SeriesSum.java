import java.util.Scanner;

public class AS2_SeriesSum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the value of n: ");
        int n = sc.nextInt();

        int sum = 0;
        int term = 1;

        while (term <= n) {
            sum = sum + term;

            if (term == 1)
                term = 5;
            else
                term = term + 5;
        }

        System.out.println("Sum of the series = " + sum);
    }
}