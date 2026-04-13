// Class demonstrating final variable
class College {

    // final variable (constant)
    final String COLLEGE_NAME = "IIT Bombay";

    // Method to display the constant value
    void display() {
        System.out.println("College Name (Constant): " + COLLEGE_NAME);
    }
}

// Main class
public class FinalVariable {
    public static void main(String[] args) {

        // Create object
        College c1 = new College();

        // Display constant value
        c1.display();
    }
}
