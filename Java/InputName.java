import java.util.Scanner;

class InputName {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = sc.nextLine();

        System.out.println("Welcome " + name + " to Java Lab");
    }
}