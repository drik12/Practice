class ThreadLifecycleDemo extends Thread {

    public void run() {
        try {
            System.out.println("Inside run() - State: " + Thread.currentThread().getState());

            Thread.sleep(500); // TIMED_WAITING state

        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {

        ThreadLifecycleDemo t = new ThreadLifecycleDemo();

        // 1. NEW state
        System.out.println("After creation - State: " + t.getState());

        // 2. RUNNABLE state
        t.start();
        System.out.println("After start() - State: " + t.getState());

        try {
            Thread.sleep(100); // Let thread enter sleep

            // 3. TIMED_WAITING state
            System.out.println("During sleep - State: " + t.getState());

            t.join(); // Wait for thread to finish

        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // 4. TERMINATED state
        System.out.println("After completion - State: " + t.getState());
    }
}