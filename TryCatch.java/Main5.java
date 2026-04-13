import java.util.Scanner;

public class Main5{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        try {
            // Code that might raise exceptions
            System.out.print("Enter a number: ");
            int number = Integer.parseInt(sc.nextLine());
            int result = 10 / number;
            System.out.println(result);
        } catch (NumberFormatException e) {
            System.out.println("I GOT VALUE ERROR!!!... ENTER A VALID INTEGER");
        } catch (ArithmeticException e) {
            System.out.println("YOU DIVIDED SOME VALUE BY 0??");
        }
        sc.close();
    }
}