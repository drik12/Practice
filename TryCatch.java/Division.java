import java.util.Scanner;

class Division {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // INPUT
        System.out.print("Enter dividend: ");
        int a = sc.nextInt();

        System.out.print("Enter divisor: ");
        int b = sc.nextInt();

        try {
            // PROCESSING
            int result = a / b;

            // OUTPUT
            System.out.println("Result: " + result);
        }

        catch (ArithmeticException e) {
            System.out.println("Error: Division by zero is not allowed");
        }

        sc.close();
    }
}