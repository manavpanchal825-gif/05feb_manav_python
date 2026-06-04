import java.awt.event.MouseListener;
import java.awt.event.MouseEvent;
import java.applet.Applet;
import java.awt.Graphics;
public class EventHandling extends Applet implements MouseListener
{
    StringBuffer strBuffer;
    public void init()
    {
        addMouseListener(this);
        strBuffer = new StringBuffer();
        addItem("initializing the applet");
    }
    public void start()
    {
        addItem("Starting the applet");
    }
    public void stop()
    {
        addItem("stopping the applet");
    }
    public void destroy()
    {
        addItem("uploading the applet");
    }
    void addItem(String word)
    {
        System.out.println(word);
        strBuffer.append(word);
        repaint();
    }
    public void paint(Graphics g)
    {
        g.drawRect(0,0,getWidth() -1,getHeight() -1);
        g.drawString(strBuffer.toString(), 10, 20);
    }
    public void mouseEntered(MouseEvent event){
    }
    public void mouseExited(MouseEvent event){
    }
    public void mousePressed(MouseEvent event){
    }
    public void mouseReleased(MouseEvent event)
    {
    }
        public void
                mouseClicked(MouseEvent event){
                    addItem("mouse clicked!");
                }
    }
    
