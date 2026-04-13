import java.util.Scanner;

class Circle {
    double radius;

    // Method to calculate area
    void findArea() {
        double area = Math.PI * radius * radius;
        System.out.println("Area of the circle = " + area);
    }
}

public class CircleArea {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Create object of Circle class
        Circle c = new Circle();

        // Input radius from user
        System.out.print("Enter radius of the circle: ");
        c.radius = sc.nextDouble();

        // Call method using object
        c.findArea();

        sc.close();
    }
}