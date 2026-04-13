import java.util.Scanner;

public class AS2_UpperTriangularMatrix {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter order of the matrix: ");
        int n = sc.nextInt();

        int[][] matrix = new int[n][n];

        System.out.println("Enter matrix elements:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }

        boolean isUpperTriangular = true;

        // Check elements below main diagonal
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (matrix[i][j] != 0) {
                    isUpperTriangular = false;
                    break;
                }
            }
        }

        if (isUpperTriangular)
            System.out.println("The matrix is an Upper Triangular Matrix.");
        else
            System.out.println("The matrix is NOT an Upper Triangular Matrix.");
    }
}