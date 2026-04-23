import java.util.Scanner;

public class AS2_ReverseBits {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int num = sc.nextInt();

        int original = num;
        int reversed = 0;

        // Reverse 32 bits
        for (int i = 0; i < 32; i++) {
            reversed = (reversed << 1) | (num & 1);
            num = num >> 1;
        }

        // Print binaries
        System.out.println("Original number: " + original);
        System.out.println("Binary of original: " +
                String.format("%32s", Integer.toBinaryString(original)).replace(' ', '0'));

        System.out.println("Reversed bits value: " + reversed);
        System.out.println("Binary after reversing: " +
                String.format("%32s", Integer.toBinaryString(reversed)).replace(' ', '0'));
    }
}