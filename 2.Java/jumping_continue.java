public class jumping_continue {
    public static void main(String args[])
    {
        int[] Numbers={10,20,30,40,50};
        for(int x : Numbers)
        {
            if(x==20)
                continue;
            System.out.println(x);
           
        }
    }
}
