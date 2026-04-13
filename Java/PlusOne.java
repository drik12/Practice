import java.util.Arrays;

class PlusOne {
    public static int[] plusOne(int[] digits) {

        for (int i = digits.length - 1; i >= 0; i--) {

            if (digits[i] < 9) {
                digits[i]++;       // add one
                return digits;
            }

            digits[i] = 0;        // if digit is 9, make it 0
        }

        // if all digits were 9
        int[] result = new int[digits.length + 1];
        result[0] = 1;
        return result;
    }

    public static void main(String[] args) {

        int[] digits = {2, 9, 9};

        int[] answer = plusOne(digits);

        System.out.println(Arrays.toString(answer));
    }
}