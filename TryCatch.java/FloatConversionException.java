import java.util.Scanner;

class FloatConversionException {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        try {

            // INPUT
            System.out.print("Enter a value: ");
            String input = sc.nextLine();

            // PROCESSING
            float num = Float.parseFloat(input);

            // OUTPUT
            System.out.println("Conversion successful: " + num);

            // Attempt conversion of null
            String value = null;
            float nullValue = Float.parseFloat(value);

        }

        catch (NumberFormatException e) {
            System.out.println("Error: Invalid number format");
        }

        catch (NullPointerException e) {
            System.out.println("Error: Null cannot be converted to float");
        }

        sc.close();
    }
}