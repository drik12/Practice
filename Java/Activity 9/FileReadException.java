import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class FileReadException {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        try {
            // Take file name as input
            System.out.print("Enter file name: ");
            String fileName = sc.nextLine();

            // Open file
            File file = new File(fileName);
            Scanner fileReader = new Scanner(file);

            // Read file (expecting numbers)
            while (fileReader.hasNext()) {
                int data = Integer.parseInt(fileReader.next());
                System.out.println("Read number: " + data);
            }

            fileReader.close();
        } 
        catch (FileNotFoundException e) {
            System.out.println("Error: File not found.");
        } 
        catch (NumberFormatException e) {
            System.out.println("Error: Invalid data format in file.");
        } 
        finally {
            System.out.println("File operation completed.");
            sc.close();
        }
    }
}
