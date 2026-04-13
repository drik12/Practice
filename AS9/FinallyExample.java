import java.io.*;

public class FinallyExample {
    public static void main(String[] args) {
        FileReader file = null;
        BufferedReader reader = null;

        try{
            file = new FileReader("data.txt");
            reader = new BufferedReader(file);

            String line = reader.readLine();
            System.out.println("File Content: " + line);

            int x = 10/0;
        } catch (FileNotFoundException e) {
            System.out.println("Error: File not found.");
        } catch (IOException e){
            System.out.println("Error: IO problem.");
        } catch (ArithmeticException e){
            System.out.println("Error: Can not divide by zero.");
        } finally {
            System.out.println("Finally block executed.");
            try{
                if (reader != null){
                    reader.close();
                    System.out.println("BufferedReader Closed.");
                }
                if (file != null){
                    file.close();
                    System.out.println("FileReader Closed.");
                }
            } catch (IOException e){
                System.out.println("Error while closing file.");
            }
        }
    }
}
