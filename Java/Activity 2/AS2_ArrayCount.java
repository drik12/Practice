import java.util.Scanner;

public class AS2_ArrayCount {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();

        int[] arr = new int[n];

        System.out.println("Enter the elements:");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int positive = 0, negative = 0, even = 0, odd = 0;

        for (int i = 0; i < n; i++) {
            if (arr[i] > 0)
                positive++;
            else if (arr[i] < 0)
                negative++;

            if (arr[i] % 2 == 0)
                even++;
            else
                odd++;
        }

        System.out.println("Positive numbers: " + positive);
        System.out.println("Negative numbers: " + negative);
        System.out.println("Even numbers: " + even);
        System.out.println("Odd numbers: " + odd);
        sc.close();
    }
}