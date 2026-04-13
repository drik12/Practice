// Parent class
class Ride {
    void calculateFare(double distance) {
        System.out.println("Calculating ride fare");
    }
}

// Child class 1
class BikeRide extends Ride {
    @Override
    void calculateFare(double distance) {
        double fare = distance * 5;
        System.out.println("Bike Ride Fare: " + fare);
    }
}

// Child class 2
class AutoRide extends Ride {
    @Override
    void calculateFare(double distance) {
        double fare = distance * 8;
        System.out.println("Auto Ride Fare: " + fare);
    }
}

// Child class 3
class CarRide extends Ride {
    @Override
    void calculateFare(double distance) {
        double fare = distance * 12;
        System.out.println("Car Ride Fare: " + fare);
    }
}

// Main class
public class RideTest {
    public static void main(String[] args) {

        Ride r;

        r = new BikeRide();
        r.calculateFare(10);

        r = new AutoRide();
        r.calculateFare(10);

        r = new CarRide();
        r.calculateFare(10);
    }
} 