import java.util.*;

class IntegerInput{
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");

        try {
            String input = sc.nextLine();     // input
            int num = Integer.parseInt(input);     // processing

            System.out.println("Output: " + num);  // output
        }

        catch (NumberFormatException e) {
            System.out.println("Error: Invalid Integer");
        }

        sc.close();
    }
}