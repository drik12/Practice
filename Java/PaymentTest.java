class PaymentProcessor {

    // Process payment by cash
    void processPayment(double amount) {
        System.out.println("Processing cash payment of Rs. " + amount);
    }

    // Process payment by card
    void processPayment(String cardNumber, double amount) {
        System.out.println("Processing card payment of Rs. " + amount +
                           " using card number: " + cardNumber);
    }

    // Process payment by UPI
    void processPayment(String upiID, double amount, String method) {
        System.out.println("Processing UPI payment of Rs. " + amount +
                           " using UPI ID: " + upiID);
    }
}

public class PaymentTest {
    public static void main(String[] args) {

        PaymentProcessor p = new PaymentProcessor();

        p.processPayment(500);                         // cash payment
        p.processPayment("1234-5678-9012", 1000);      // card payment
        p.processPayment("user@upi", 750, "UPI");      // UPI payment
    }
}