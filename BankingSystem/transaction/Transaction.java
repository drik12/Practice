package transaction;

import account.Account;

public class Transaction {

    public void deposit(Account acc, double amount) {
        acc.setBalance(acc.getBalance() + amount);
        System.out.println("Deposited: " + amount);
    }

    public void withdraw(Account acc, double amount) {
        if (amount <= acc.getBalance()) {
            acc.setBalance(acc.getBalance() - amount);
            System.out.println("Withdrawn: " + amount);
        } else {
            System.out.println("Insufficient Balance");
        }
    }
}