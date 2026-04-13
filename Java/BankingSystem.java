import java.util.Scanner;

// Base class
class Account {

    String accountHolder;
    int accountNumber;
    double balance;

    // Input common account details
    void inputAccountDetails(Scanner sc) {

        System.out.print("Enter Account Holder Name: ");
        accountHolder = sc.nextLine();

        System.out.print("Enter Account Number: ");
        accountNumber = sc.nextInt();

        System.out.print("Enter Initial Balance: ");
        balance = sc.nextDouble();

        sc.nextLine(); // consume newline
    }

    // Display common account details
    void displayAccountDetails() {

        System.out.println("\nAccount Details");
        System.out.println("Holder Name: " + accountHolder);
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Balance: " + balance);
    }
}

// Child class 1
class SavingsAccount extends Account {

    double interestRate = 4.5;

    void displaySavingsAccount() {

        displayAccountDetails();

        System.out.println("\nSavings Account Info");
        System.out.println("Interest Rate: " + interestRate + "%");
    }
}

// Child class 2
class CurrentAccount extends Account {

    double overdraftLimit = 10000;

    void displayCurrentAccount() {

        displayAccountDetails();

        System.out.println("\nCurrent Account Info");
        System.out.println("Overdraft Limit: " + overdraftLimit);
    }
}

// Main class
public class BankingSystem {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Choose Account Type:");
        System.out.println("1. Savings Account");
        System.out.println("2. Current Account");
        System.out.print("Enter choice: ");
        int choice = sc.nextInt();

        sc.nextLine(); // consume newline

        if (choice == 1) {

            SavingsAccount s1 = new SavingsAccount();
            s1.inputAccountDetails(sc);
            s1.displaySavingsAccount();

        } else if (choice == 2) {

            CurrentAccount c1 = new CurrentAccount();
            c1.inputAccountDetails(sc);
            c1.displayCurrentAccount();

        } else {
            System.out.println("Invalid Choice!");
        }

        sc.close();
    }
}
