import java.util.Scanner;

public class AS3_CopyArray {

    // Method to copy array elements
    public static int[] copyArray(int[] arr) {
        int[] newArray = new int[arr.length];

        for (int i = 0; i < arr.length; i++) {
            newArray[i] = arr[i];
        }

        return newArray;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] original = new int[10];

        System.out.println("Enter 10 integers:");
        for (int i = 0; i < original.length; i++) {
            original[i] = sc.nextInt();
        }

        int[] copied = copyArray(original);

        System.out.println("Copied array elements:");
        for (int i = 0; i < copied.length; i++) {
            System.out.println(copied[i]);
        }

        sc.close();
    }
}