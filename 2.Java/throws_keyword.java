import java.io.*;
public class throws_keyword {
    void method()throws IOException
    {
        throw new IOException("device error");
    }
}
class throws_keywordthrow
{
    public static void main(String args[])
    {
        try
        {
           throws_keyword obj=new throws_keyword();
            obj.method();
        }
        catch(Exception e){System.out.println("exception handled"+e);}
        System.out.println("normal flow...");
    }
            
}
 