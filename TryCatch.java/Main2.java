public class Main2 {

    public static void main(String[] args) {

        int i = 0;

        while (i < 2) {

            int a = 10;
            int b = 0;
            int c;

            try {
                c = a / b;   // This will raise an ArithmeticException
            }
            catch (ArithmeticException e) {
                System.out.println("Error: Invalid value of c");
                c = 0; // Assigning a default value to prevent a crash
            }

            System.out.println("This line will also be printed, as our program is not crashed");

            i++;
        }
    }
}