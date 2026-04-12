class ComputeTask implements Runnable {
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println("Computing: " + (i * i));
            try { Thread.sleep(500); } catch (Exception e) {}
        }
    }
}

class LogTask implements Runnable {
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println("Logging data " + i);
            try { Thread.sleep(700); } catch (Exception e) {}
        }
    }
}

class DisplayTask implements Runnable {
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println("Displaying result " + i);
            try { Thread.sleep(600); } catch (Exception e) {}
        }
    }
}

public class MultiThreadSystem {
    public static void main(String[] args) {

        // Create Runnable objects
        Runnable compute = new ComputeTask();
        Runnable log = new LogTask();
        Runnable display = new DisplayTask();

        // Create Threads
        Thread t1 = new Thread(compute);
        Thread t2 = new Thread(log);
        Thread t3 = new Thread(display);

        // Start Threads (run concurrently)
        t1.start();
        t2.start();
        t3.start();
    }
}