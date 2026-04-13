class Temperature {
    
    //Convert celsius to farenheight
    double convert(double celsius) {
        return (celsius * 9/5) + 32;
    }

    //Convert celsius to kelvin
    double convert(double celsius, double k) {
        return celsius + 273.15;
    }

    public static void main(String []args) {
        Temperature t = new Temperature();

        double f = t.convert(25);        
        double k = t.convert(25, 1.0);   

        System.out.println("Celsius to Fahrenheit: " + f);
        System.out.println("Celsius to Kelvin: " + k);
    }

}
