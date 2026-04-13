// Base class
class Notification {

    // Method to send general notification
    void sendAlert() {
        System.out.println("Sending general notification.");
    }
}

// Child class
class EmailNotification extends Notification {

    // Overriding the parent class method
    @Override
    void sendAlert() {
        System.out.println("Sending email notification.");
    }
}

// Main class
public class NotificationTest {

    public static void main(String[] args) {

        Notification n;

        n = new Notification();
        n.sendAlert();          // calls parent class method

        n = new EmailNotification();
        n.sendAlert();          // calls child class overridden method
    }
}