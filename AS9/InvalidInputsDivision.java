import java.util.Scanner;

public class InvalidInputsDivision {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        try {

            System.out.println("Enter Dividend: ");
            String input1 = sc.nextLine();

            System.out.println("Enter Divisor: ");
            String input2 = sc.nextLine();

            int a = Integer.parseInt(input1);
            int b = Integer.parseInt(input2);

            int result = a / b;

            System.out.println("Result: " + result);

        }

        catch (NumberFormatException e) {
            System.out.println("Invalid Input! Please enter numbers only.");
        }

        catch (ArithmeticException e) {
            System.out.println("Division by Zero is not accepted");
        }

        finally {
            System.out.println("Operation Completed.");
        }

        sc.close();

    }
}
