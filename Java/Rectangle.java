class Rectangle {
    double length;
    double breadth;

    //Constuctor to initialize values
    Rectangle(double l, double b) {
        length = l;
        breadth = b;
    }
    //Method to calculate area
    double area() {
        return length * breadth;
    }

    public static void main(String []args) {
        //Create object and pass values to constuctor
        Rectangle r1 = new Rectangle(10,5);
        
        //Calculate and display area
        System.out.println("Length: " + r1.length);
        System.out.println("Breadth: " + r1.breadth);
        System.out.println("Area: " + r1.area());
    }
}
