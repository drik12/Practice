class MyThread1 extends Thread {
    public void run() {
        for (int i = 1; i <= 3; i++) {
            System.out.print("A");
            try {
            Thread.sleep(10);
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }
    }
}

class MyThread2 extends Thread {
    public void run() {
        for (int i = 1; i <= 3; i++) {
            System.out.print("B");
            try {
            Thread.sleep(10);
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }
    }
}


public class TestThread2 {
    public static void main(String[] args) {
        MyThread1 t1 = new MyThread1();
        MyThread2 t2 = new MyThread2();

        t1.start();
        t2.start();
    }
}