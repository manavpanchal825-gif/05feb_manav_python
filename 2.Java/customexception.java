class InvalidAgeExp extends Exception
{
    InvalidAgeExp(String s)
    {super(s);}
}
public class customexception {
    static void Validate(int age)throws InvalidAgeExp
    {
        if(age<18)
            throw new InvalidAgeExp("not valid");
        else
                System.out.println("welcome to vote");
    }
    public static void main(String args[])
    {
        try
        {
            Validate(24);
        }
        catch(Exception e){System.out.println("Exception occured:"+e);}
        System.out.println("rest of the code...");
    }
    
}
