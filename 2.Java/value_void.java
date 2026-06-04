public class value_void
{
    double width, height, depth;

    void volume()
    {
        System.out.println("Volume is: " + (width * height * depth));
    }

    public static void main(String args[])
    {
        value_void mybox1 = new value_void();
        value_void mybox2 = new value_void();

        mybox1.width = 10;
        mybox1.height = 20;
        mybox1.depth = 15;

        mybox2.width = 10;
        mybox2.height = 15;
        mybox2.depth = 25;

        mybox1.volume();
        mybox2.volume();
    }
}
