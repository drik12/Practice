import java.util.Scanner;

public class AS2_ArraySearch {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();

        int[] arr = new int[n];

        System.out.println("Enter the elements:");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        System.out.print("Enter element to search: ");
        int key = sc.nextInt();

        int count = 0;

        for (int i = 0; i < n; i++) {
            if (arr[i] == key) {
                count++;
            }
        }

        if (count > 0) {
            System.out.println("Element " + key + " found " + count + " time(s).");
        } else {
            System.out.println("Element not found in the array.");
        }
        sc.close();
    }
}