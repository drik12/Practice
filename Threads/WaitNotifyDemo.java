class Shared {
    int data;
    boolean hasData = false;

    public synchronized void produce(int value) {
        while (hasData) {
            try {
                wait(); // wait if data not consumed
            } catch (InterruptedException e) {}
        }

        data = value;
        hasData = true;
        System.out.println("Produced: " + value);

        notify(); // notify consumer
    }

    public synchronized void consume() {
        while (!hasData) {
            try {
                wait(); // wait until data is produced
            } catch (InterruptedException e) {}
        }

        System.out.println("Consumed: " + data);
        hasData = false;

        notify(); // notify producer
    }
}
class Producer extends Thread {
    Shared shared;

    Producer(Shared s) {
        shared = s;
    }

    public void run() {
        for (int i = 1; i <= 5; i++) {
            shared.produce(i);
        }
    }
}
class Consumer extends Thread {
    Shared shared;

    Consumer(Shared s) {
        shared = s;
    }

    public void run() {
        for (int i = 1; i <= 5; i++) {
            shared.consume();
        }
    }
}
public class WaitNotifyDemo {
    public static void main(String[] args) {
        Shared shared = new Shared();

        Producer p = new Producer(shared);
        Consumer c = new Consumer(shared);

        p.start();
        c.start();
    }
}