import java.io.*;
public class RnadomIO 
{
    public static void main(String args[])
    {
        RandomAccessFile file=null;
        try
        {
           file=new  RandomAccessFile("Test.txt","rw");
           //writing to the file
           file.writeChar('X');
           file.writeInt(555);
           file.writeDouble(3.1412);
           file.seek(0);//go to the beginning
           //reading from the file
           System.out.println(file.readChar());
           System.out.println(file.readInt());
           System.out.println(file.readDouble());
           file.seek(2);
           System.out.println(file.readInt());
           file.close();
        }
        catch(IOException e)
        {
            System.out.println("Excption:"+ e);
        }
    }
}
