class Book {
    String title;
    double price;

    //Parameterized Constructor
    Book(String t, double p){
        title = t;
        price = p;
    }
    void displayDetails() {
        System.out.println("Title: " + title);
        System.out.println("Price: " + price);
    }
    public static void main(String []args) {
        Book b1 = new Book("Java Programming", 499.99);
        b1.displayDetails();
    }
}
