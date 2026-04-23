package AS8;

interface Printable{
    void print();
}

interface Scannable{
    void Scan();
}

class MultiFunctionDevice implements Printable, Scannable {

    public void print() {
        System.out.println("Printing Document....");
    }
    public void Scan() {
        System.out.println("Scanning Document....");
    }
}

public class Main7 {
    public static void main(String[] args) {
        MultiFunctionDevice device = new MultiFunctionDevice();

        device.print();
        device.Scan();
    }
}
