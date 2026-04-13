class NullInputException extends Exception{
    public NullInputException(String message) {
        super(message);
    }
}

class InvalidFormatException extends Exception{
    public InvalidFormatException(String message) {
        super(message);
    }
}

class AuthenticationException extends Exception{
    public AuthenticationException(String message) {
        super(message);
    }
}
class Login {

    public void login(String username, String password)
            throws NullInputException, InvalidFormatException, AuthenticationException{
        if (username == null || password == null) {
            throw new NullInputException("Nothing Entered."); 
        } 
        else if(username.length()< 5 || password.length()< 6){
            throw new InvalidFormatException("Invalid Format! Username or password too short.");
        }

        else if(!username.equals("admin") || !password.equals("123456")){
            throw new AuthenticationException("Invalid Credentials.");
        }

        else{
            System.out.println("Login Successful!");    
        }
    }
}

public class LoginSystem {
    public static void main(String[] args) {
        Login obj = new Login();

        try{
            obj.login("admin", "123456");
        } catch (NullInputException e) {
            System.out.println("Error: " + e.getMessage());
        } catch (InvalidFormatException e) {
            System.out.println("Error: " + e.getMessage());
        } catch (AuthenticationException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
