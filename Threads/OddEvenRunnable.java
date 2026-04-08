class EvenRunnable implements Runnable {
    public void run() {
        for (int i = 1; i <= 10; i++) {
            if (i % 2 == 0) {
                System.out.println("Even: " + i);
            }
        }
    }
}

class OddRunnable implements Runnable {
    public void run() {
        for (int i = 1; i <= 10; i++) {
            if (i % 2 != 0) {
                System.out.println("Odd: " + i);
            }
        }
    }
}

public class OddEvenRunnable {
    public static void main(String[] args) {

        Thread t1 = new Thread(new EvenRunnable());
        Thread t2 = new Thread(new OddRunnable());

        t1.start();
        t2.start();
    }
}