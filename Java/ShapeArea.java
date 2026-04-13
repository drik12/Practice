class ShapeArea {

    // Area of circle
    double area(double radius) {
        return 3.14 * radius * radius;
    }

    // Area of rectangle
    double area(double length, double breadth) {
        return length * breadth;
    }

    public static void main(String[] args) {
        ShapeArea s = new ShapeArea();

        // Circle area
        double circleArea = s.area(5);  
        System.out.println("Area of Circle: " + circleArea);

        // Rectangle area
        double rectArea = s.area(10, 4);
        System.out.println("Area of Rectangle: " + rectArea);
    }
}
