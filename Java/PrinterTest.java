class Printer {

    // Method to print a number
    void print(int number) {
        System.out.println("Printing number: " + number);
    }

    // Method to print text
    void print(String text) {
        System.out.println("Printing text: " + text);
    }

    // Method to print both number and text
    void print(int number, String text) {
        System.out.println("Printing number and text: " + number + " - " + text);
    }
}

public class PrinterTest {
    public static void main(String[] args) {

        Printer p = new Printer();

        p.print(25);                     // prints number
        p.print("Hello Printer");        // prints text
        p.print(10, "Pages Printed");    // prints both
    }
}