import java.util.Scanner;

public class AS2_DuplicateCharacters {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a string: ");
        String str = sc.nextLine();

        char[] chars = str.toCharArray();

        System.out.println("Duplicate characters are:");

        for (int i = 0; i < chars.length; i++) {
            int count = 1;

            if (chars[i] == '0') {
                continue;
            }

            for (int j = i + 1; j < chars.length; j++) {
                if (chars[i] == chars[j]) {
                    count++;
                    chars[j] = '0'; // mark as counted
                }
            }
            if (count > 1 && chars[i] != ' ') {
                System.out.println(chars[i]);
            }
        }
        sc.close();
    }

}