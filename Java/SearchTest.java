class SearchUtility {

    // Search integer in integer array
    void search(int[] arr, int key) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == key) {
                System.out.println("Integer found at index: " + i);
                return;
            }
        }
        System.out.println("Integer not found");
    }

    // Search string in string array
    void search(String[] arr, String key) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i].equals(key)) {
                System.out.println("String found at index: " + i);
                return;
            }
        }
        System.out.println("String not found");
    }

    // Search integer within a given index range
    void search(int[] arr, int key, int start, int end) {
        for (int i = start; i <= end; i++) {
            if (arr[i] == key) {
                System.out.println("Integer found at index: " + i);
                return;
            }
        }
        System.out.println("Integer not found in given range");
    }
}

public class SearchTest {
    public static void main(String[] args) {

        SearchUtility s = new SearchUtility();

        int[] numbers = {10, 20, 30, 40, 50};
        String[] words = {"apple", "banana", "orange"};

        s.search(numbers, 30);
        s.search(words, "banana");
        s.search(numbers, 40, 2, 4);
    }
}