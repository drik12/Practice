import java.util.Scanner;

public class AS3_RowColumnSum {

    // Method to calculate row-wise sum
    public static void rowWiseSum(int[][] matrix, int rows, int cols) {
        for (int i = 0; i < rows; i++) {
            int sum = 0;
            for (int j = 0; j < cols; j++) {
                sum += matrix[i][j];
            }
            System.out.println("Sum of row " + (i + 1) + " = " + sum);
        }
    }

    // Method to calculate column-wise sum
    public static void columnWiseSum(int[][] matrix, int rows, int cols) {
        for (int j = 0; j < cols; j++) {
            int sum = 0;
            for (int i = 0; i < rows; i++) {
                sum += matrix[i][j];
            }
            System.out.println("Sum of column " + (j + 1) + " = " + sum);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int rows, cols;

        System.out.print("Enter number of rows: ");
        rows = sc.nextInt();

        System.out.print("Enter number of columns: ");
        cols = sc.nextInt();

        int[][] matrix = new int[rows][cols];

        System.out.println("Enter matrix elements:");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }

        rowWiseSum(matrix, rows, cols);
        columnWiseSum(matrix, rows, cols);

        sc.close();
    }
}