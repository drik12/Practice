public class Exercise6 {

    public static void main(String[] args) {

        int count = 0;

        for (int i = 1; i <= 100; i++) {
            if (i % 5 == 0) {
                count++;
            }
        }

        System.out.println("Numbers divisible by 5 between 1 and 100: " + count);
    }
}