import java.util.Scanner;

class BankAccount {
    int accNumber;
    double balance;

    // Method to deposit amount
    void deposit(double amount) {
        balance = balance + amount;
        System.out.println("Amount Deposited: " + amount);
    }

    // Method to withdraw amount
    void withdraw(double amount) {
        if (amount <= balance) {
            balance = balance - amount;
            System.out.println("Amount Withdrawn: " + amount);
        } else {
            System.out.println("Insufficient Balance!");
        }
    }

    // Method to display account details
    void display() {
        System.out.println("\nAccount Details");
        System.out.println("Account Number: " + accNumber);
        System.out.println("Current Balance: " + balance);
    }
}

public class BankAccountDemo {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Create object
        BankAccount b = new BankAccount();

        // Input account details
        System.out.print("Enter Account Number: ");
        b.accNumber = sc.nextInt();

        System.out.print("Enter Initial Balance: ");
        b.balance = sc.nextDouble();

        // Deposit
        System.out.print("Enter amount to Deposit: ");
        double depAmt = sc.nextDouble();
        b.deposit(depAmt);

        // Withdraw
        System.out.print("Enter amount to Withdraw: ");
        double withAmt = sc.nextDouble();
        b.withdraw(withAmt);

        // Display final details
        b.display();

        sc.close();
    }
}