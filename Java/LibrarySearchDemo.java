import java.util.Scanner;

class Book {
    String title;
    String author;

    // Constructor to assign book details
    Book(String title, String author) {
        this.title = title;
        this.author = author;
    }

    // Method to display book details
    void display() {
        System.out.println("Book Title: " + title);
        System.out.println("Author Name: " + author);
    }
}

public class LibrarySearchDemo {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Store multiple book objects
        Book[] books = new Book[3];

        books[0] = new Book("Java Programming", "James Gosling");
        books[1] = new Book("Python Basics", "Guido van Rossum");
        books[2] = new Book("C Language", "Dennis Ritchie");

        // Input title to search
        System.out.print("Enter book title to search: ");
        String searchTitle = sc.nextLine();

        boolean found = false;

        // Search book by title using equals()
        for (int i = 0; i < books.length; i++) {
            if (books[i].title.equals(searchTitle)) {
                System.out.println("\nBook Found!");
                books[i].display();
                found = true;
                break;
            }
        }

        if (!found) {
            System.out.println("\nBook Not Found in Library!");
        }

        sc.close();
    }
}
