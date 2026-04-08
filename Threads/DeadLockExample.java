// Shared resources class
class Resources {
    static final Object resource1 = new Object();
    static final Object resource2 = new Object();
}

// Thread 1 class
class Thread1 extends Thread {

    public void run() {

        synchronized (Resources.resource1) {
            System.out.println("Thread 1: Locked Resource 1");

            try { Thread.sleep(100); }
            catch (InterruptedException e) {}

            System.out.println("Thread 1: Waiting for Resource 2");

            synchronized (Resources.resource2) {
                System.out.println("Thread 1: Locked Resource 2");
            }
        }
    }
}

// Thread 2 class
class Thread2 extends Thread {

    public void run() {

        synchronized (Resources.resource2) {
            System.out.println("Thread 2: Locked Resource 2");

            try { Thread.sleep(100); }
            catch (InterruptedException e) {}

            System.out.println("Thread 2: Waiting for Resource 1");

            synchronized (Resources.resource1) {
                System.out.println("Thread 2: Locked Resource 1");
            }
        }
    }
}

// Main class
public class DeadLockExample {

    public static void main(String[] args) {

        Thread1 t1 = new Thread1();
        Thread2 t2 = new Thread2();

        t1.start();
        t2.start();
    }
}