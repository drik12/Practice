public class Main {

    public static void main(String[] args) {

        while (true) {

            int a = 10;
            int b = 0;

            try {
                int c = a / b;
                System.out.println(c);
            }
            catch (ArithmeticException e) {
                System.out.println("Invalid value of c");
            }

        }
    }
}