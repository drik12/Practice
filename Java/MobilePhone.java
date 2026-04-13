class MobilePhone{
    String brand;
    double price;

    //Constructor 1: Only brand name
    MobilePhone(String b) {
        brand = b;
        price = 0.0;
    }

    //Constructor 2: Brand name and price
    MobilePhone(String b, double p) {
        brand = b;
        price = p;
    }

    //Method to display details
    void display(){
        System.out.println("Brand: " + brand);
        System.out.println("Price: " + price);
    }

    public static void main(String[] args) {
        //Object with only brand
        MobilePhone m1 = new MobilePhone("Samsung");
        //Object with brand and price
        MobilePhone m2 = new MobilePhone("Apple", 79999);
        m1.display();
        m2.display();
    }
}