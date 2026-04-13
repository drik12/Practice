public class BalancedBrackets {
    public static void main(String[] args) {

        String str = "{[()]}";
        char[] arr = new char[str.length()];
        int top = -1;

        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);

            // opening brackets
            if (c == '(' || c == '{' || c == '[') {
                arr[++top] = c;
            }
            else {
                if (top == -1) {
                    System.out.println("Invalid");
                    return;
                }

                char last = arr[top--];

                if ((c == ')' && last != '(') ||
                    (c == '}' && last != '{') ||
                    (c == ']' && last != '[')) {
                    System.out.println("Invalid");
                    return;
                }
            }
        }

        if (top == -1)
            System.out.println("Valid");
        else
            System.out.println("Invalid");
    }
}