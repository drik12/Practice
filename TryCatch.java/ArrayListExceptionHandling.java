import java.util.Scanner;
import java.util.ArrayList;

class ArrayListExceptionHandling {

    public static void main(String[] args) {

        // Create and initialize ArrayList
        ArrayList<Integer> myList = new ArrayList<>();
        myList.add(1);
        myList.add(2);
        myList.add(5);
        myList.add(9);
        myList.add(10);
        myList.add(11);

        Scanner scanner = new Scanner(System.in);

        try {

            // INPUT
            System.out.print("Enter index: ");
            String input = scanner.nextLine();

            // PROCESSING
            int index = Integer.parseInt(input);
            int value = myList.get(index);

            // OUTPUT
            System.out.println("Element at index " + index + " is: " + value);

        } 
        catch (NumberFormatException e) {
            System.out.println("Error: Please enter a valid number");
        } 
        catch (IndexOutOfBoundsException e) {
            System.out.println("Error: Index out of range");
        }

        scanner.close();
    }
}