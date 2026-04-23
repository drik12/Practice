package Java.AS8;

interface Payment {
    void processPayment(double amount);
}

class CreditCard implements Payment{
    public void processPayment(double amount){
        System.out.println("Processing Credit Card payment of ₹" + amount);
    }
}

class UPI implements Payment {
    public void processPayment(double amount){
        System.out.println("Processing UPI payment of ₹" + amount);
    }
}

public class Main4 {
    public static void main(String[] args){
        Payment p1 = new CreditCard();
        Payment p2 = new UPI();

        p1.processPayment(1800);
        p2.processPayment(800);
    }
}
