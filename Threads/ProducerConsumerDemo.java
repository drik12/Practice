// Shared buffer class
class Buffer {

    int data;
    boolean hasData = false; // flag

    // Producer method
    public synchronized void produce(int value) {

        // If buffer is full, wait
        while (hasData) {
            try {
                wait();
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }

        // Produce data
        data = value;
        System.out.println("Produced: " + data);

        hasData = true;

        // Notify consumer
        notify();
    }

    // Consumer method
    public synchronized void consume() {

        // If buffer is empty, wait
        while (!hasData) {
            try {
                wait();
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }

        // Consume data
        System.out.println("Consumed: " + data);

        hasData = false;

        // Notify producer
        notify();
    }
}

// Producer thread
class Producer extends Thread {

    Buffer buffer;

    Producer(Buffer buffer) {
        this.buffer = buffer;
    }

    public void run() {

        for (int i = 1; i <= 5; i++) {
            buffer.produce(i);
        }
    }
}

// Consumer thread
class Consumer extends Thread {

    Buffer buffer;

    Consumer(Buffer buffer) {
        this.buffer = buffer;
    }

    public void run() {

        for (int i = 1; i <= 5; i++) {
            buffer.consume();
        }
    }
}

// Main class
public class ProducerConsumerDemo {

    public static void main(String[] args) {

        Buffer buffer = new Buffer();

        Producer p = new Producer(buffer);
        Consumer c = new Consumer(buffer);

        p.start();
        c.start();
    }
}