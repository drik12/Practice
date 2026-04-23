import java.util.Scanner;

public class AS2_ReverseArrayCopy {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();

        int[] arr1 = new int[n];
        int[] arr2 = new int[n];

        System.out.println("Enter the elements:");
        for (int i = 0; i < n; i++) {
            arr1[i] = sc.nextInt();
        }

        // Copy elements in reverse order
        for (int i = 0; i < n; i++) {
            arr2[i] = arr1[n - 1 - i];
        }

        System.out.println("Original Array:");
        for (int i = 0; i < n; i++) {
            System.out.print(arr1[i] + " ");
        }

        System.out.println("\nReversed Copied Array:");
        for (int i = 0; i < n; i++) {
            System.out.print(arr2[i] + " ");
        }
    }
}