import java.util.Scanner;

// Base class
class Vehicle {

    String vehicleNumber;
    String fuelType;

    // Input common vehicle details
    void inputVehicleDetails(Scanner sc) {

        System.out.print("Enter Vehicle Number: ");
        vehicleNumber = sc.nextLine();

        System.out.print("Enter Fuel Type: ");
        fuelType = sc.nextLine();
    }

    // Display common vehicle details
    void displayVehicleDetails() {

        System.out.println("\nVehicle Details");
        System.out.println("Vehicle Number: " + vehicleNumber);
        System.out.println("Fuel Type: " + fuelType);
    }
}

// Child class 1: Bus
class Bus extends Vehicle {

    int passengerCapacity;

    void inputBusDetails(Scanner sc) {

        System.out.print("Enter Passenger Capacity: ");
        passengerCapacity = sc.nextInt();
    }

    void displayBusDetails() {

        displayVehicleDetails();

        System.out.println("\nBus Specific Details");
        System.out.println("Passenger Capacity: " + passengerCapacity);
    }
}

// Child class 2: Truck
class Truck extends Vehicle {

    double loadCapacity;

    void inputTruckDetails(Scanner sc) {

        System.out.print("Enter Load Capacity (in tons): ");
        loadCapacity = sc.nextDouble();
    }

    void displayTruckDetails() {

        displayVehicleDetails();

        System.out.println("\nTruck Specific Details");
        System.out.println("Load Capacity: " + loadCapacity + " tons");
    }
}

// Main class
public class TransportSystem {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Choose Vehicle Type:");
        System.out.println("1. Bus");
        System.out.println("2. Truck");
        System.out.print("Enter choice: ");
        int choice = sc.nextInt();

        sc.nextLine(); // consume newline

        if (choice == 1) {

            Bus b1 = new Bus();
            b1.inputVehicleDetails(sc);
            b1.inputBusDetails(sc);

            System.out.println("\nBus Information");
            b1.displayBusDetails();

        } else if (choice == 2) {

            Truck t1 = new Truck();
            t1.inputVehicleDetails(sc);
            t1.inputTruckDetails(sc);

            System.out.println("\nTruck Information");
            t1.displayTruckDetails();

        } else {
            System.out.println("Invalid Choice!");
        }

        sc.close();
    }
}
