import javax.swing.*;
import java.awt.event.*;

public class ComboBoxDemo {
    public static void main(String[] args) {
        JFrame frame = new JFrame("ComboBox Calculator");

        // Components
        JTextField t1 = new JTextField();
        JTextField t2 = new JTextField();
        JTextField result = new JTextField();

        String ops[] = {"+", "-", "*", "/"};
        JComboBox<String> box = new JComboBox<>(ops);

        // Set positions
        t1.setBounds(50, 30, 100, 30);
        t2.setBounds(200, 30, 100, 30);
        box.setBounds(150, 30, 50, 30);
        result.setBounds(100, 100, 120, 30);

        // Add event to JComboBox
        box.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                try {
                    int a = Integer.parseInt(t1.getText());
                    int b = Integer.parseInt(t2.getText());
                    String op = (String) box.getSelectedItem();
                    int res = 0;

                    switch (op) {
                        case "+": res = a + b; break;
                        case "-": res = a - b; break;
                        case "*": res = a * b; break;
                        case "/": res = a / b; break;
                    }

                    result.setText(String.valueOf(res));
                } catch (Exception ex) {
                    result.setText("Error");
                }
            }
        });

        // Add components
        frame.add(t1);
        frame.add(t2);
        frame.add(box);
        frame.add(result);

        frame.setSize(350, 200);
        frame.setLayout(null);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}