class A extends Thread
{
    public void run()
    {
        for(int i=1;i<5;i++)
            System.out.println("from Thread a:i="+i);
        System.out.println("Exit from A");
    }
}
class B extends Thread
{
    public void run()
    {
        for(int i=1;i<5;i++)
            System.out.println("From Thread b:i="+i);
        System.out.println("Exit from B");
    }
}
public class multi_thread 
{
    public static void main(String args[])
    {
        A a= new A();
        B b= new B();
        a.start();
        b.start();
    }
}
