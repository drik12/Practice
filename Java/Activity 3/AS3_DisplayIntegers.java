import java.util.Scanner;

public class AS3_DisplayIntegers {

    // Method to display array elements
    public static void displayArray(int[] arr) {
        System.out.println("The entered integers are:");
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] numbers = new int[10];

        // Taking input
        System.out.println("Enter 10 integers:");
        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = sc.nextInt();
        }

        // Passing array to method
        displayArray(numbers);

        sc.close();
    }
}