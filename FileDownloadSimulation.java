class Download {
    int progress = 0;
    boolean running = true;
}

// Thread 1: Simulates download
class Downloader extends Thread {
    Download d;

    Downloader(Download d) {
        this.d = d;
    }

    public void run() {
        for (int i = 0; i <= 100; i++) {
            d.progress = i;
            try {
                Thread.sleep(50); // simulate download time
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }
        d.running = false;
    }
}

// Thread 2: Displays progress
class Display extends Thread {
    Download d;

    Display(Download d) {
        this.d = d;
    }

    public void run() {
        while (d.running) {
            System.out.println("Progress: " + d.progress + "%");
            try {
                Thread.sleep(100); // refresh display
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }
        System.out.println("Download Complete!");
    }
}

public class FileDownloadSimulation {
    public static void main(String[] args) {
        Download d = new Download();

        Downloader t1 = new Downloader(d);
        Display t2 = new Display(d);

        t1.start();
        t2.start();
    }
}