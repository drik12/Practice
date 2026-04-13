import java.util.Scanner;

public class AS2_Determinant5x5 {

    // Method to get determinant of a matrix
    static int determinant(int[][] matrix, int n) {
        int det = 0;

        // Base case for 1x1 matrix
        if (n == 1)
            return matrix[0][0];

        int[][] submatrix = new int[n - 1][n - 1];
        int sign = 1;

        // Laplace expansion along first row
        for (int col = 0; col < n; col++) {
            int subi = 0;
            for (int i = 1; i < n; i++) {
                int subj = 0;
                for (int j = 0; j < n; j++) {
                    if (j == col)
                        continue;
                    submatrix[subi][subj] = matrix[i][j];
                    subj++;
                }
                subi++;
            }
            det += sign * matrix[0][col] * determinant(submatrix, n - 1);
            sign = -sign;
        }
        return det;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] matrix = new int[5][5];

        System.out.println("Enter elements of 5x5 matrix:");
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }

        int det = determinant(matrix, 5);
        System.out.println("Determinant of the matrix = " + det);
    }
}