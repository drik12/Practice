import java.util.Scanner;

interface Printer {
    void print();
}

class TextPrinter implements Printer {
    public void print() {
        System.out.println("Printing text document...");
    }
}

class ImagePrinter implements Printer {
    public void print() {
        System.out.println("Printing image...");
    }

}

public class Main2 {
    public static void main(String[] args){
        Printer p1 = new TextPrinter();
        Printer p2 = new ImagePrinter();

        p1.print();
        p2.print(); 
    }
}
