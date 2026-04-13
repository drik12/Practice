// Custom Exception Class
class InsufficientBalanceException extends Exception {
    public InsufficientBalanceException(String message) {
        super(message);
    }
}

// Bank Account Class
class BankAccount {
    private double balance;

    // Constructor
    public BankAccount(double balance) {
        this.balance = balance;
    }

    // Withdraw Method
    public void withdraw(double amount) throws InsufficientBalanceException {
        if (amount > balance) {
            // Throw exception if balance is insufficient
            throw new InsufficientBalanceException("Insufficient balance! Withdrawal failed.");
        } else {
            balance -= amount;
            System.out.println("Withdrawal successful. Remaining balance: " + balance);
        }
    }
}

// Main Class
public class BankingSystem {
    public static void main(String[] args) {
        BankAccount account = new BankAccount(5000);

        try {
            account.withdraw(6000); // This will cause exception
        } catch (InsufficientBalanceException e) {
            // Catching the exception
            System.out.println("Error: " + e.getMessage());
        }

        try {
            account.withdraw(2000); // This will work
        } catch (InsufficientBalanceException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}