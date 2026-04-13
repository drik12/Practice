import java.util.Scanner;

class Complex {
    double real, imaginary;

    // Method to add two complex numbers
    Complex add(Complex c1, Complex c2) {
        Complex result = new Complex();
        result.real = c1.real + c2.real;
        result.imaginary = c1.imaginary + c2.imaginary;
        return result;
    }

    // Method to display complex number
    void display() {
        System.out.println(real + " + " + imaginary + "i");
    }
}

public class ComplexAdditionDemo {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Create objects
        Complex c1 = new Complex();
        Complex c2 = new Complex();
        Complex c3 = new Complex();

        // Input first complex number
        System.out.print("Enter real part of first complex number: ");
        c1.real = sc.nextDouble();

        System.out.print("Enter imaginary part of first complex number: ");
        c1.imaginary = sc.nextDouble();

        // Input second complex number
        System.out.print("Enter real part of second complex number: ");
        c2.real = sc.nextDouble();

        System.out.print("Enter imaginary part of second complex number: ");
        c2.imaginary = sc.nextDouble();

        // Add complex numbers
        c3 = c3.add(c1, c2);

        // Display result
        System.out.println("\nFirst Complex Number: ");
        c1.display();

        System.out.println("Second Complex Number: ");
        c2.display();

        System.out.println("Sum of Complex Numbers: ");
        c3.display();

        sc.close();
    }
}
