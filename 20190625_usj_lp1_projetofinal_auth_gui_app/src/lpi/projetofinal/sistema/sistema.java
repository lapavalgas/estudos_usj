package lpi.projetofinal.sistema;

import javax.swing.JOptionPane;
import lpi.projetofinal.entity.User;
import lpi.projetofinal.gui.*;

public class sistema {
    
    public static User user;

    public static void main(String[] args) {
        
        Login login = new Login();
        login.setVisible(true);
        
    }
    
}
