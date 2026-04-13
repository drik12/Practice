package main;

import account.Account;
import transaction.Transaction;
import report.Report;

public class Main {

    public static void main(String[] args) {

        Account acc = new Account("12345", 1000);

        Transaction t = new Transaction();
        Report r = new Report();

        t.deposit(acc, 500);
        t.withdraw(acc, 200);

        r.showBalance(acc);
    }
}