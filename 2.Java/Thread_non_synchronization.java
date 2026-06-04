class PrintStr
{
    static void print(String s1, String s2)
    {
        System.out.println(s1 + ":");
        try
        {
            Thread.sleep(400);
        }
        catch(InterruptedException e)
        {
            System.out.println("Interrupted");
        }
        System.out.println(s2);
    }
}

class StrThread implements Runnable
{
    Thread t;
    String s1, s2;

    StrThread(String s1, String s2)
    {
        this.s1 = s1;
        this.s2 = s2;
        t = new Thread(this, "My Thread");
        t.start();
    }

    public void run()
    {
        PrintStr.print(s1, s2);
    }
}

public class Thread_non_synchronization
{
    public static void main(String args[])
    {
        System.out.println("Non Synchronization Example");

        new StrThread("1", "one");
        new StrThread("2", "two");
        new StrThread("3", "three");
    }
}
