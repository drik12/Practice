import java.util.Scanner;

public class p3 {
    public static void main(String[] args) {

        Scanner bill = new Scanner(System.in);

        System.out.print("Enter the bill amount: ");
        int billAmount = bill.nextInt();

        if(billAmount > 1000) {
            System.out.print("Discount is applicable" );
        } else {
            System.out.print( "Discount is not applicable" );
        }
        
        bill.close();
    }

}
