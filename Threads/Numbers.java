class PrintNumbersThread extends Thread{
    public void run(){
        for (int i = 1; i <= 10; i++){
            System.out.println("Numbers: " + i);
            try{
                Thread.sleep(1000);
            }

            catch(InterruptedException e){
                System.out.println(e);
            }
        }
    }
}

public class Numbers{
    public static void main(String[] args) {
        PrintNumbersThread t1 = new PrintNumbersThread();

        t1.start();
    }
}