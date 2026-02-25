public class finalizemethod {
    int a;
    public static void main(String args[])
    {
        finalizemethod obj= new finalizemethod();
        obj.a=10;
        System.out.println(obj.a);
        obj=null;
        System.gc();
        System.out.println("end of garbage collection");
    }
    protected void finalize()
    {
        System.out.println("finelize method called");
    }
    
}
