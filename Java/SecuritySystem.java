// Final class (cannot be inherited)
final class SecurityHelper {

    void encryptData() {
        System.out.println("Data is being encrypted securely...");
    }

    void decryptData() {
        System.out.println("Data is being decrypted securely...");
    }
}

// Main class
public class SecuritySystem {
    public static void main(String[] args) {

        // Create object of final class
        SecurityHelper helper = new SecurityHelper();

        helper.encryptData();
        helper.decryptData();

        // Not allowed:
        // class Hacker extends SecurityHelper  Error (cannot inherit final class)
    }
}
