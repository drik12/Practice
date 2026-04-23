import java.util.Scanner;

public class AS2_UpperToLower {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter an uppercase letter: ");
        char ch = sc.next().charAt(0);

        // Check if character is uppercase
        if (ch >= 'A' && ch <= 'Z') {
            ch = (char)(ch + 32);  // Convert to lowercase
            System.out.println("Lowercase letter: " + ch);
        } else {
            System.out.println("Entered character is not an uppercase letter.");
        }
    }
}