// Shared class
class Message {

    String msg;
    boolean ready = false;

    // Method to produce message
    public synchronized void produce(String message) {

        msg = message;
        ready = true;

        System.out.println("Produced: " + msg);

        // Notify waiting thread
        notify();
    }

    // Method to consume message
    public synchronized void consume() {

        // Wait until message is ready
        while (!ready) {
            try {
                wait(); // thread waits
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }

        System.out.println("Consumed: " + msg);
    }
}

// Producer thread
class Producer extends Thread {

    Message m;

    Producer(Message m) {
        this.m = m;
    }

    public void run() {
        m.produce("Hello World");
    }
}

// Consumer thread
class Consumer extends Thread {

    Message m;

    Consumer(Message m) {
        this.m = m;
    }

    public void run() {
        m.consume();
    }
}

// Main class
public class WaitNotifyDemo {

    public static void main(String[] args) {

        Message m = new Message();

        Consumer c = new Consumer(m);
        Producer p = new Producer(m);

        c.start(); // start consumer first (it will wait)
        p.start(); // producer notifies
    }
}