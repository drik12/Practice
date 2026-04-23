public class ProcessNumbers {
    public static void main(String[] args) {

        String[] numbers = {"10", "20", "abc", "30", "5x", "40"};

        for (int i = 0; i < numbers.length; i++) {

            try {
                System.out.println("Processing: " + numbers[i]);

                int num = Integer.parseInt(numbers[i]); // may throw exception

                int result = 100 / num; // may throw exception

                System.out.println("Result: " + result);

            } catch (NumberFormatException e) {
                System.out.println("Invalid number format: " + numbers[i]);

            } catch (ArithmeticException e) {
                System.out.println("Cannot divide by zero: " + numbers[i]);
            }

            System.out.println("----------------------");
        }

        System.out.println("Processing completed.");
    }
}
