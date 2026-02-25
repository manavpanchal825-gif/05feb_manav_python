public class calculation1 {
    void sum(int a, int b)
    {
        System.out.println(a+b);
    }
    void sum(int a,int b,int c)
    {
        System.out.println(a+b+c);
    }
}
class caldemo
{
    public static void main(String args[])
    {
        calculation1 c=new calculation1();
        c.sum(10,10,10);
        c.sum(20, 20);
    }
}