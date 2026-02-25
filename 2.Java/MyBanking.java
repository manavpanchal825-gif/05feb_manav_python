class Banking 
{
    double p; // principal
    double r; // rate of interest
    int n;    // number of years

    double simpleInterest() 
    {
        return (p * r * n) / 100;
    }
}
class NewBanking extends Banking 
{
    NewBanking(double pa, double roi, int noy)
    {
        p = pa;
        r = roi;
        n = noy;
    }
    double compoundInterest() 
    {
        double ci = p * Math.pow(1 + r / 100, n);
        return ci - p;
    }
}
public class MyBanking {
    public static void main(String[] args) 
    {
        NewBanking nb = new NewBanking(1000,12,5);
        double si = nb.simpleInterest();
        double ci = nb.compoundInterest();
        System.out.println("Simple Interest is: " + si);
        System.out.println("Compound Interest is: " + ci);
    }
}
