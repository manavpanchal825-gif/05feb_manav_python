import java.io.*;
public class BufferedInputOutput
{
    public static void main(String args[])
    {
        try
        {
            FileInputStream fin= new FileInputStream("f1.txt");
            BufferedInputStream bin = new BufferedInputStream(fin);
            FileOutputStream fout = new FileOutputStream("f2.txt");
            BufferedOutputStream bout= new BufferedOutputStream(fout);
            int i;
            while((i=bin.read())!=-1)
            {bout.write((byte)i);}
            bin.close();
            fin.close();
            bout.close();
            fout.close();
            System.out.println("success");
        }
        catch(Exception e)
        { System.out.println(e);  }
    }
}
