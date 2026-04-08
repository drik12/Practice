// Class to demonstrate thread priority
class PriorityDemo extends Thread {

    // Constructor to set thread name
    PriorityDemo(String name) {
        super(name);
    }

    // run() method
    public void run() {

        // Loop to print thread info
        for (int i = 1; i <= 5; i++) {

            // Print thread name and priority
            System.out.println(
                "Thread: " + Thread.currentThread().getName() +
                " | Priority: " + Thread.currentThread().getPriority()
            );
        }
    }
}

// Main class
public class ThreadPriorityExample {

    public static void main(String[] args) {

        // Create threads
        PriorityDemo t1 = new PriorityDemo("Low Priority Thread");
        PriorityDemo t2 = new PriorityDemo("Medium Priority Thread");
        PriorityDemo t3 = new PriorityDemo("High Priority Thread");

        // Set priorities
        t1.setPriority(Thread.MIN_PRIORITY);   // 1
        t2.setPriority(Thread.NORM_PRIORITY);  // 5
        t3.setPriority(Thread.MAX_PRIORITY);   // 10

        // Start threads
        t1.start();
        t2.start();
        t3.start();
    }
}