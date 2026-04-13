class DiscountCalculator {

    // Discount based on price only
    void calculateDiscount(double price) {
        double discount = price * 0.05;   // 5% discount
        System.out.println("Discount: " + discount);
    }

    // Discount based on price and membership
    void calculateDiscount(double price, String membership) {
        double discount;

        if (membership.equals("Gold"))
            discount = price * 0.10;
        else
            discount = price * 0.07;

        System.out.println("Discount with membership: " + discount);
    }

    // Discount based on price, membership, and coupon
    void calculateDiscount(double price, String membership, String coupon) {
        double discount = price * 0.15;   // 15% discount
        System.out.println("Discount with membership and coupon: " + discount);
    }
}

public class DiscountTest {
    public static void main(String[] args) {

        DiscountCalculator d = new DiscountCalculator();

        d.calculateDiscount(1000);
        d.calculateDiscount(1000, "Gold");
        d.calculateDiscount(1000, "Gold", "SAVE20");
    }
}