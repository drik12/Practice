import java.util.Scanner;

public class AS3_LargestElement {

    // Method to find the largest element in the array
    public static int findLargest(int[] arr) {
        int largest = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > largest) {
                largest = arr[i];
            }
        }
        return largest;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] numbers = new int[10];

        System.out.println("Enter 10 integers:");
        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = sc.nextInt();
        }

        int largestElement = findLargest(numbers);

        System.out.println("Largest element in the array: " + largestElement);

        sc.close();
    }
}