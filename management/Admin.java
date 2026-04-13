package management;

public class Admin {
    public void manage() {
        Student s = new Student();
        Course c = new Course();

        s.display();
        c.display();

        System.out.println("Admin managing system");
    }
}