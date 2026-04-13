class Calculator {
    //Method for adding integers
    int add(int a, int b) {
        return a + b;
    }
    //Method for adding floating point numbers
    double add(double a, double b) {
        return a + b;
    }
    public static void main(String[] args) {
        Calculator c = new Calculator();

        //Integer addition
        int sum1 = c.add(10, 20);
        System.out.println("Integer Sum: " + sum1);

        //Floating point addition
        double sum2 = c.add(5.5, 2.3);
        System.out.println("Float Sum: " + sum2);
    }
}
