import java.util.Scanner;

public class ArrayException {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int[] arr = {10, 20, 30, 40, 50};

        System.out.println("Enter Index to access: ");
        int index = sc.nextInt();

        try{
            System.out.println("Element: " + arr[index]);
        }

        catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Exception Caught!");
            System.out.println("Index " + index + " is out of bounds.");
        }
        sc.close();
    }
}
