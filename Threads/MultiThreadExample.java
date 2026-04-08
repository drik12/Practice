// Class to print even numbers
class EvenThread extends Thread {

    // Override run() method (entry point of thread)
    public void run() {

        // Loop from 1 to 10
        for (int i = 1; i <= 10; i++) {

            // Check if number is even
            if (i % 2 == 0) {

                // Print even number
                System.out.println("Even: " + i);
            }

            // Small delay to visualize thread execution
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }
    }
}

// Class to print odd numbers
class OddThread extends Thread {

    // Override run() method
    public void run() {

        // Loop from 1 to 10
        for (int i = 1; i <= 10; i++) {

            // Check if number is odd
            if (i % 2 != 0) {

                // Print odd number
                System.out.println("Odd: " + i);
            }

            // Delay for better interleaving
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }
    }
}

// Main class
public class MultiThreadExample {

    public static void main(String[] args) {

        // Create thread objects
        EvenThread t1 = new EvenThread();
        OddThread t2 = new OddThread();

        // Start both threads
        t1.start();
        t2.start();
    }
}