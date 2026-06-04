import java.io.*;
public class BufferedDemo
{
    public static void main(String args[])
    {
        try
        {
            FileWriter writer= new FileWriter("E:\\testout.txt");
            BufferedWriter buffer= new BufferedWriter(writer);
            buffer.write("Welcome TO World Of JAVA.");
            buffer.close();
            
            FileReader fr = new FileReader("E:\\testout.txt");
            BufferedReader br= new BufferedReader(fr);
            String ln=null;
            while((ln=br.readLine())!=null)
            {
                System.out.println(ln);
            }
            br.close();
        }
        catch(Exception e){System.out.println(e);}
    }
}
