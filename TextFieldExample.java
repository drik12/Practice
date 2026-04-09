import javax.swing.*;
import java.awt.event.*;

public class TextFieldExample {
    public static void main(String[] args) {
        // Create frame
        JFrame frame = new JFrame("Input Checker");

        // Create components
        JTextField textField = new JTextField();
        JButton button = new JButton("Submit");

        // Set bounds (position & size)
        textField.setBounds(50, 50, 200, 30);
        button.setBounds(100, 100, 100, 30);

        // Add event handling
        button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String input = textField.getText();

                if (input.isEmpty()) {
                    JOptionPane.showMessageDialog(frame, "Error: Field is empty!");
                } else {
                    JOptionPane.showMessageDialog(frame, "You entered: " + input);
                }
            }
        });

        // Add components to frame
        frame.add(textField);
        frame.add(button);

        // Frame settings
        frame.setSize(300, 200);
        frame.setLayout(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}