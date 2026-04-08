// Thread 1 class
class HelloThread extends Thread {

    // run() method contains thread logic
    public void run() {

        // Print Hello 5 times
        for (int i = 0; i < 5; i++) {
            System.out.println("Hello");

            try {
                Thread.sleep(500); // delay for clarity
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }
    }
}

// Thread 2 class
class WorldThread extends Thread {

    public void run() {

        // Print World 5 times
        for (int i = 0; i < 5; i++) {
            System.out.println("World");

            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }
    }
}

// Main class
public class HelloWorldThreads {

    public static void main(String[] args) {

        // Create thread objects
        HelloThread t1 = new HelloThread();
        WorldThread t2 = new WorldThread();

        // Start threads
        t1.start();
        t2.start();
    }
}