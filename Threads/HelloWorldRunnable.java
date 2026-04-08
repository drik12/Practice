class HelloRunnable implements Runnable {
    public void run() {
        System.out.println("Hello");
    }
}

class WorldRunnable implements Runnable {
    public void run() {
        System.out.println("World");
    }
}

public class HelloWorldRunnable {
    public static void main(String[] args) {

        Thread t1 = new Thread(new HelloRunnable());
        Thread t2 = new Thread(new WorldRunnable());

        t1.start();
        t2.start();
    }
}