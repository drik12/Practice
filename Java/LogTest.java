class Logger {

    // Log only message
    void log(String message) {
        System.out.println("Message: " + message);
    }

    // Log message with timestamp
    void log(String message, String timestamp) {
        System.out.println("Message: " + message + " | Timestamp: " + timestamp);
    }

    // Log message with timestamp and error code
    void log(String message, String timestamp, int errorCode) {
        System.out.println("Message: " + message + 
                           " | Timestamp: " + timestamp + 
                           " | Error Code: " + errorCode);
    }
}

public class LogTest {
    public static void main(String[] args) {

        Logger logger = new Logger();

        logger.log("System started");
        logger.log("File not found", "10:30 AM");
        logger.log("Database error", "10:45 AM", 404);
    }
}