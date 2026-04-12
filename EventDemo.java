import javax.swing.*;
import java.awt.event.*;

public class EventDemo {
    public static void main(String[] args) {

        JFrame frame = new JFrame("Keyboard & Mouse Events");

        JTextArea area = new JTextArea();
        area.setBounds(50, 50, 300, 150);

        JLabel label = new JLabel("Event Output:");
        label.setBounds(50, 220, 300, 30);

        // KeyListener
        area.addKeyListener(new KeyListener() {
            public void keyPressed(KeyEvent e) {
                label.setText("Key Pressed: " + e.getKeyChar());
            }

            public void keyReleased(KeyEvent e) {
                label.setText("Key Released: " + e.getKeyChar());
            }

            public void keyTyped(KeyEvent e) {
                label.setText("Key Typed: " + e.getKeyChar());
            }
        });

        // MouseListener
        area.addMouseListener(new MouseListener() {
            public void mouseClicked(MouseEvent e) {
                label.setText("Mouse Clicked at (" + e.getX() + "," + e.getY() + ")");
            }

            public void mousePressed(MouseEvent e) {
                label.setText("Mouse Pressed");
            }

            public void mouseReleased(MouseEvent e) {
                label.setText("Mouse Released");
            }

            public void mouseEntered(MouseEvent e) {
                label.setText("Mouse Entered Area");
            }

            public void mouseExited(MouseEvent e) {
                label.setText("Mouse Exited Area");
            }
        });

        // Frame settings
        frame.add(area);
        frame.add(label);

        frame.setSize(400, 350);
        frame.setLayout(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);

        // Important for keyboard events
        area.setFocusable(true);
    }
}