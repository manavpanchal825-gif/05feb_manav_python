import java.io.*;
public class STDemo 
{
    public static void main(String args[])throws IOException
    {
        FileReader freader=new FileReader("D:\\neenu\\bca4_manav\\src\\AIIContent.txt");
        StreamTokenizer st= new  StreamTokenizer(freader);
        double sum=0;
        int numWords=0;
        while(st.nextToken()!=st.TT_EOF)
        {
            if(st.ttype==StreamTokenizer.TT_NUMBER)
            {sum+=st.nval;}
            else if(st.ttype==StreamTokenizer.TT_WORD)
            {numWords++;}
        }
        System.out.println("sum of total numbers in the file:"+sum);
        System.out.println("Total words(doesn't include number)in the file:"+numWords);
    }
}
