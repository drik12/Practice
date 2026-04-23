import java.util.Scanner;

public class AS3_SumOfArray {

    // Method to calculate sum of array elements
    public static int findSum(int[] arr) {
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
        }
        return sum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] numbers = new int[10];

        System.out.println("Enter 10 integers:");
        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = sc.nextInt();
        }

        int result = findSum(numbers);

        System.out.println("Sum of array elements: " + result);

        sc.close();
    }
}