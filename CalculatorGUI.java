import javax.swing.*;
import java.awt.event.*;

public class CalculatorGUI {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Calculator");

        // Components
        JTextField t1 = new JTextField();
        JTextField t2 = new JTextField();
        JTextField result = new JTextField();

        String operations[] = {"+", "-", "*", "/"};
        JComboBox<String> box = new JComboBox<>(operations);

        JButton btn = new JButton("Calculate");

        // Set positions
        t1.setBounds(50, 30, 100, 30);
        t2.setBounds(200, 30, 100, 30);
        box.setBounds(150, 30, 50, 30);
        btn.setBounds(100, 80, 120, 30);
        result.setBounds(100, 130, 120, 30);

        result.setEditable(false);

        // Event Handling
        btn.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                try {
                    double num1 = Double.parseDouble(t1.getText());
                    double num2 = Double.parseDouble(t2.getText());

                    String op = (String) box.getSelectedItem();
                    double res = 0;

                    if (op.equals("+")) res = num1 + num2;
                    else if (op.equals("-")) res = num1 - num2;
                    else if (op.equals("*")) res = num1 * num2;
                    else if (op.equals("/")) res = num1 / num2;

                    result.setText(String.valueOf(res));

                } catch (Exception ex) {
                    JOptionPane.showMessageDialog(frame, "Invalid Input!");
                }
            }
        });

        // Add components
        frame.add(t1);
        frame.add(t2);
        frame.add(box);
        frame.add(btn);
        frame.add(result);

        frame.setSize(350, 250);
        frame.setLayout(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}