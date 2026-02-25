import java.util.*;
public class testimportjavautil {
    public static void main(String args[])
    {
        LinkedList<String>al=new LinkedList<String>();
        al.add("ravi");
        al.add("vijay");
        al.add("ravi");
        al.add("ajay");
        Iterator<String>itr=al.iterator();
        while(itr.hasNext())
        {
            System.out.println(itr.next());
        }
    }
    
}
