import java.util.Scanner;

public class p4 {
    public static void main(String[] args) {
        Scanner checkLeapyear = new Scanner(System.in);

        System.out.println("Enter a year: ");
        int year = checkLeapyear.nextInt();

        if (year % 400 == 0) {
            System.out.println(year + "is a leap year.");
        } else if (year % 100 == 0) {
            System.out.println(year + "is not a leap year.");
        } else if (year % 4 == 0) {
            System.out.println(year + "is a leap year.");
        } else {
            System.out.println(year + " is not a leap year");
        }

        checkLeapyear.close();
    }
}
