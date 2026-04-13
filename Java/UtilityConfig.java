// Utility class with fixed configuration values
class Config {

    // Fixed values (constants)
    static final String APP_NAME = "Banking System";
    static final int MAX_USERS = 1000;
    static final double VERSION = 1.0;

    // Method to display configuration
    static void displayConfig() {

        System.out.println("Configuration Settings");
        System.out.println("Application Name: " + APP_NAME);
        System.out.println("Maximum Users: " + MAX_USERS);
        System.out.println("Version: " + VERSION);
    }
}

// Main class
public class UtilityConfig {
    public static void main(String[] args) {

        // Display configuration values
        Config.displayConfig();

        // Not allowed to change constants
        // Config.MAX_USERS = 2000;  Error (final value cannot be modified)
    }
}