// Booking behavior
interface BookingService {
    void bookRide(String pickup, String drop);
}

// Payment behavior
interface PaymentService {
    void makePayment(double amount);
}

class RideBooking implements BookingService {

    @Override
    public void bookRide(String pickup, String drop) {
        System.out.println("Ride booked from " + pickup + " to " + drop);
    }
}

class OnlinePayment implements PaymentService {

    @Override
    public void makePayment(double amount) {
        System.out.println("Paid ₹" + amount + " using online payment");
    }
}

class CashPayment implements PaymentService {

    @Override
    public void makePayment(double amount) {
        System.out.println("Paid ₹" + amount + " in cash");
    }
}

public class RideApp {
    public static void main(String[] args) {

        BookingService booking = new RideBooking();
        booking.bookRide("Chennai", "Airport");

        PaymentService payment1 = new OnlinePayment();
        payment1.makePayment(250);

        PaymentService payment2 = new CashPayment();
        payment2.makePayment(250);
    }
}