import javax.swing.*;

public class Hello extends JFrame {
    public Hello() {
        super("Hello World");
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        add(new JLabel("Hello, world!"));
        pack();
        setVisible(true);
    }
    public void GoodBye() {
    	
    }
    public static void main(String[] args) {
        SwingUtilities.invokeLater(Hello::new);
    }
}

