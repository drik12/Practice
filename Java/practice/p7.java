import java.util.Scanner;

public class p7 {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the value of n: ");
        int num = sc.nextInt();

        int sum = 0;
        for (int i = 1; i <= num; i++) {
            if (i % 2 == 0) {
                sum = sum + i;
            }
        }

        System.out.println("Sum of even numbers from 1 to " + num + " is: " + sum);

        sc.close();
    }

}
