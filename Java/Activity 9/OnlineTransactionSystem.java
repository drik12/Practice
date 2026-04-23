class InsufficientBalanceException extends Exception {
    public InsufficientBalanceException(String message) {
        super(message);
    }
}

class OnlineTransactionSystem {

    static double balance = 5000.0;

    public static void processTransaction(Double amount) {
        try {
            // Check for null input
            if (amount == null) {
                throw new NullPointerException("Amount cannot be null");
            }

            // Check for invalid amount
            if (amount <= 0) {
                throw new IllegalArgumentException("Invalid transaction amount");
            }

            // Simulate arithmetic exception
            int test = 10 / 1; // change to 0 to test ArithmeticException

            // Check balance
            if (amount > balance) {
                throw new InsufficientBalanceException("Insufficient balance");
            }

            // Process transaction
            balance -= amount;
            System.out.println("Transaction successful!");
            System.out.println("Remaining balance: " + balance);

        } catch (NullPointerException e) {
            System.out.println("Error: " + e.getMessage());

        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());

        } catch (InsufficientBalanceException e) {
            System.out.println("Error: " + e.getMessage());

        } catch (ArithmeticException e) {
            System.out.println("Math Error: " + e.getMessage());

        } catch (Exception e) {
            System.out.println("General Error: " + e.getMessage());

        } finally {
            System.out.println("Transaction attempt completed.\n");
        }
    }

    public static void main(String[] args) {

        // Test cases
        processTransaction(1000.0);   // valid
        processTransaction(6000.0);   // insufficient balance
        processTransaction(-500.0);   // invalid amount
        processTransaction(null);     // null input
    }
}
