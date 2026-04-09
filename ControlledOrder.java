class MyThread1 extends Thread {
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.print(i + " ");
        }
    }
}

class MyThread2 extends Thread {
    public void run() {
        for (int i = 100; i <= 105; i++) {
            System.out.print(i + " ");
        }
    }
}

public class ControlledOrder {
    public static void main(String[] args) throws InterruptedException {
        MyThread1 t1 = new MyThread1();
        MyThread2 t2 = new MyThread2();

        t1.start();
        t1.join();

        t2.start();
        t2.join();
    }
}