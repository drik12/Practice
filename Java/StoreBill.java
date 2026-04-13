public class StoreBill {
    public static void main(String[] args) {

        // Prices
        double priceA = 200;
        double priceB = 75;
        double priceC = 500;

        // Quantities
        int qtyA = 2;
        int qtyB = 1;
        int qtyC = 3;

        // Item A calculation
        double totalA = priceA * qtyA;
        totalA = totalA - (totalA * 0.10);  // 10% discount
        totalA = totalA + (totalA * 0.05);  // 5% tax

        // Item B calculation
        double totalB = priceB * qtyB;
        totalB = totalB - (totalB * 0.10);
        totalB = totalB + (totalB * 0.05);

        // Item C calculation
        double totalC = priceC * qtyC;
        totalC = totalC - (totalC * 0.10);
        totalC = totalC + (totalC * 0.05);

        // Final amount
        double finalAmount = totalA + totalB + totalC;

        System.out.println("Final Amount to Pay: " + finalAmount);
    }
}