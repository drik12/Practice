class Student {
    String name;
    int age;

    //Default Constructor (no arguments)
    Student() {
        name = "Rahul";
        age = 20;
    }
    //Method to display details
    void display() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }

    public static void main(String []args){
        //Object created using default constructor
        Student s1 = new Student();

        //Display default values
        s1.display();
    }
}
