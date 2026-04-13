import java.util.Scanner;

public class p5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter value of a: ");
        int a = sc.nextInt();

        System.out.print("Enter value of b: ");
        int b = sc.nextInt();

        System.out.print("Enter value of a: ");
        int c = sc.nextInt();

        if (a >= b && a>= c) {
            System.out.print("a is the greatest number.");
        } else if (b >= a && b >= c) {
            System.out.print("b is the greatest number.");
        } else {
            System.out.print("b is the greatest number.");
        }
        sc.close();
    }
}
