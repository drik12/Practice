// Parent class
class Vehicle {

    String brand = "Toyota";

    // Parent class constructor
    Vehicle() {
        System.out.println("Vehicle Constructor Called");
    }
}

// Child class
class Car extends Vehicle {

    String brand = "Honda";

    // Child class constructor
    Car() {
        super(); // Calls parent constructor

        System.out.println("Car Constructor Called");
    }

    // Method to display brands
    void displayBrand() {

        System.out.println("Car Brand: " + brand);

        // Access parent class variable using super
        System.out.println("Vehicle Brand: " + super.brand);
    }
}

// Main class
public class SuperKeyword {
    public static void main(String[] args) {

        // Create Car object
        Car c1 = new Car();

        // Display parent and child data
        c1.displayBrand();
    }
}
