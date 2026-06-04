public class dispatch 
{
    public void type()
    {
        System.out.println("indoor & outdoor");
    }
}

class Cricket extends dispatch 
{
    public void type() 
    {
        System.out.println("outdoor game");
    }

    public static void main(String[] args) 
    {
            dispatch gm=new dispatch();
            Cricket ck=new Cricket();
            gm.type();
            ck.type();
            gm=ck;
           gm.type();
      
    }
}
