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

public class UncontrolledOrder {
    public static void main(String[] args) {
        MyThread1 t1 = new MyThread1();
        MyThread2 t2 = new MyThread2();

        t1.start();
        t2.start();
    }
}
//Why output order varies:
//Threads execute independently.
//The JVM + OS scheduler switches between threads.
//No guarantee which thread finishes first.
