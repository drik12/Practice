class TicketBooking {
    private int availableSeats;

    public TicketBooking(int seats) {
        this.availableSeats = seats;
    }

    // synchronized method to prevent race condition
    public synchronized void bookTicket(String user, int seatsRequested) {
        System.out.println(user + " trying to book " + seatsRequested + " seats...");

        if (seatsRequested <= availableSeats) {
            System.out.println("Booking successful for " + user);
            availableSeats -= seatsRequested;
            System.out.println("Seats left: " + availableSeats);
        } else {
            System.out.println("Booking failed for " + user + " (Not enough seats)");
        }
    }
}

// Thread class
class UserThread extends Thread {
    TicketBooking booking;
    String userName;
    int seats;

    public UserThread(TicketBooking booking, String userName, int seats) {
        this.booking = booking;
        this.userName = userName;
        this.seats = seats;
    }

    public void run() {
        booking.bookTicket(userName, seats);
    }
}

// Main class
public class Main {
    public static void main(String[] args) {

        TicketBooking booking = new TicketBooking(5); // Only 5 seats available

        // Multiple users trying to book at same time
        UserThread t1 = new UserThread(booking, "Alice", 2);
        UserThread t2 = new UserThread(booking, "Bob", 3);
        UserThread t3 = new UserThread(booking, "Charlie", 2);

        t1.start();
        t2.start();
        t3.start();
    }
}