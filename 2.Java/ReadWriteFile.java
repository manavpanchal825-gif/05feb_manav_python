import java.io.*;
public class ReadWriteFile
{
    public static void main(String args[])throws Exception
    {
        FileInputStream fin= new FileInputStream("Test.txt");
        FileOutputStream fout= new FileOutputStream("T.txt");
        int i=0;
        while((i=fin.read())!=-1)
        {
            fout.write((byte)i);
        }
        System.out.println(" 1 File Copied");
        fin.close();
        fout.close();
        fin = new FileInputStream("T.txt");
        while((i=fin.read())!=-1)
        {
            System.out.print((char)i);
        }
        fin.close();
    }
}
