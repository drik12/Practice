import java.util.Scanner;

public class p8 {
    public static void main(String[]args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter a number: ");
        int number = sc.nextInt();

        int sum = 0;
        int temp = number;

        while (temp > 0) {
            int digit = temp % 10;
            sum = sum + digit;
            temp = temp / 10;
        }

        if (sum % 2 == 0) {
            System.out.println(number + " is a special number");
        } else {
            System.out.println(number + " is not a special number");
        }

        sc.close();
        
    }
}
