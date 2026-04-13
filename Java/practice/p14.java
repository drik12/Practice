import java.util.Scanner;

public class p14 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter an uppercase letter: ");
        char ch = sc.next().charAt(0);

        if(ch >= 'A' & ch <= 'Z') {
            ch = (char)(ch + 32);
            System.out.println("Lowercase letter: " + ch);
        } else {
            System.out.println("Entered letter is not an uppercase letter.");
        }
    }
}
