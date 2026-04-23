import java.util.Scanner;

public class AS3_CountArrayElements {

    // Method to count positive numbers
    public static int countPositive(int[] arr) {
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > 0) {
                count++;
            }
        }
        return count;
    }

    // Method to count negative numbers
    public static int countNegative(int[] arr) {
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] < 0) {
                count++;
            }
        }
        return count;
    }

    // Method to count even numbers
    public static int countEven(int[] arr) {
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] % 2 == 0) {
                count++;
            }
        }
        return count;
    }

    // Method to count odd numbers
    public static int countOdd(int[] arr) {
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] % 2 != 0) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] numbers = new int[10];

        System.out.println("Enter 10 integers:");
        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = sc.nextInt();
        }

        System.out.println("Positive elements: " + countPositive(numbers));
        System.out.println("Negative elements: " + countNegative(numbers));
        System.out.println("Even elements: " + countEven(numbers));
        System.out.println("Odd elements: " + countOdd(numbers));

        sc.close();
    }
}
