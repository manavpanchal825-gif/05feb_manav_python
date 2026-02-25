import java.applet.*;
import java.awt.*;
import java.util.Date;
public class GFG1 extends Applet
{
   public void paint(Graphics g)
   {
       Date dt = new Date();
       super.showStatus("Today is"+dt);
   }
}
