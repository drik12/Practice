import java.util.Scanner;

public class AS3_CountEvenElements {

    // Method to count even elements in the array
    public static int countEven(int[] arr) {
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] % 2 == 0) {
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

        int evenCount = countEven(numbers);

        System.out.println("Number of even elements: " + evenCount);

        sc.close();
    }
}