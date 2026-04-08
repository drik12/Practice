// Shared resource class
class Counter {

    int count = 0; // shared variable

    // Method to increment count
    public void increment() {

        // Not synchronized → race condition occurs
        count++;
    }
}

// Thread class
class MyThread extends Thread {

    Counter counter; // shared object

    // Constructor
    MyThread(Counter counter) {
        this.counter = counter;
    }

    public void run() {

        // Increment 1000 times
        for (int i = 0; i < 1000; i++) {
            counter.increment();
        }
    }
}

// Main class
public class RaceConditionDemo {

    public static void main(String[] args) throws InterruptedException {

        Counter counter = new Counter();

        // Create two threads
        MyThread t1 = new MyThread(counter);
        MyThread t2 = new MyThread(counter);

        // Start threads
        t1.start();
        t2.start();

        // Wait for both threads to finish
        t1.join();
        t2.join();

        // Expected output = 2000
        System.out.println("Final Count: " + counter.count);
    }
}