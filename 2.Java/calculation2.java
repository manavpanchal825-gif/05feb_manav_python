public class calculation2 {
    void sum(int a,int b)
    {
        System.out.println(a+b);
    }
    void sum(double a, double b)
    {
        System.out.println(a+b);
    }
    void sum(float a, float b)
    {
        System.out.println(a+b);
    }
}
class calDemo
{
    public static void main(String args[])
    {
        calculation2 c=new calculation2();
        c.sum(10,20);
        c.sum(20.5,30.5);
        c.sum(10.5f, 20.6);
    }
}