// Shared Counter class
class Counter {

    int count = 0; // shared variable

    // synchronized method to avoid race condition
    public synchronized void increment() {
        count++;
    }
}

// Thread class
class MyThread extends Thread {

    Counter counter;

    // Constructor
    MyThread(Counter counter) {
        this.counter = counter;
    }

    // Thread execution
    public void run() {

        // Increment 1000 times
        for (int i = 1; i <= 1000; i++) {
            counter.increment();
        }
    }
}

// Main class
public class SharedCounterDemo {

    public static void main(String[] args) throws InterruptedException {

        // Create shared object
        Counter counter = new Counter();

        // Create threads
        MyThread t1 = new MyThread(counter);
        MyThread t2 = new MyThread(counter);

        // Start threads
        t1.start();
        t2.start();

        // Wait for completion
        t1.join();
        t2.join();

        // Print final result
        System.out.println("Final Count: " + counter.count);
    }
}