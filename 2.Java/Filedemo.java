import java.io.*;

public class Filedemo
{
    public static void main(String args[])
    {
        try
        {
            File file = new File("e:\\java_ex\\test.txt");

            if (file.isFile())
            {
                System.out.println("File exists");
            }
            else
            {
                System.out.println("File does not exist");
            }
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
    }
}
