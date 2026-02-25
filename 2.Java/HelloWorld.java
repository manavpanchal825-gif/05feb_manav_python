import java.applet.Applet;
import java.awt.Graphics;
public class HelloWorld extends Applet
{
    //Overriding paint ()method 
 
 public void paint(Graphics g)
    {
        g.drawString("Hello World", 20, 20);
    }
}
