 class printstr
{
  synchronized static void print(String s1, String s2)
    {
        System.out.print(s1 + ":");
        try
        {Thread.sleep(400);}
            catch(InterruptedException e)
            {System.out.println("Interrupted");}
            System.out.println(s2);        
    }
}
class strThread implements Runnable
{
    Thread t;
    String s1 , s2;
    strThread(String s1 , String s2)
    {
        this.s1 =s1;
        this.s2 =s2;
        t = new Thread(this, "My Thread");
        t.start();
    }
    public void run()
    {
        printstr.print( s1 , s2 );
    }
}
public class thread_Synchronized
{
    public static void main(String args[])
    {
        System.out.println("Synchronized ex");
        new strThread( "1", "one" );
        new strThread( "2", "two");
        new strThread( "3", "three");
    }
}
