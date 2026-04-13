class BankAccount {
    int accountNumber;
    double balance;

    //Constructor 1: Only account number
    BankAccount(int accNo) {
        accountNumber = accNo;
        balance = 0.0;
    }

    //Constructor 2: Account Number + initial balance
    BankAccount(int accNo, double bal) {
        accountNumber = accNo;
        balance = bal;
    }

    //Method to display account details
    void display(){
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Balance: " + balance);
    }

    public static void main(String[] args) {
        //Account created with only account number
        BankAccount a1 = new BankAccount(1001);
        //Account created with account number and initial balance
        BankAccount a2 = new BankAccount(1002, 5000);

        a1.display();
        a2.display();

    }
}
