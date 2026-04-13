package report;

import account.Account;

public class Report {

    public void showBalance(Account acc) {
        System.out.println("Account No: " + acc.getAccountNumber());
        System.out.println("Balance: " + acc.getBalance());
    }
}