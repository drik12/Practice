import java.util.Scanner;

public class students_marks2 {

    public static void main(String[] args) {

        int maths, phy, che, eng, compsc;
        double finalscore;
        int studentNumber;

        Scanner marks = new Scanner(System.in);

        System.out.print("Enter number of students: ");
        studentNumber = marks.nextInt();

        for (int i = 1; i <= studentNumber; i++) {

            System.out.println("Student " + i);

            System.out.print("Enter Marks for Maths: ");
            maths = marks.nextInt();

            System.out.print("Enter Marks for Phy: ");
            phy = marks.nextInt();

            System.out.print("Enter Marks for Che: ");
            che = marks.nextInt();

            System.out.print("Enter Marks for Eng: ");
            eng = marks.nextInt();

            System.out.print("Enter Marks for CompSc: ");
            compsc = marks.nextInt();

            finalscore = (maths + phy + che + eng + compsc) / 5.0;

            if (finalscore > 90)
                System.out.println("Excellent");
            else if (finalscore > 80)
                System.out.println("V.Good");
            else if (finalscore > 60)
                System.out.println("Good");
            else if (finalscore > 40)
                System.out.println("Average");
            else
                System.out.println("Poor");
        }

        marks.close();
    }
}