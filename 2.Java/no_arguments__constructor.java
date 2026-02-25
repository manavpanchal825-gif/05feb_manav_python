public class no_arguments__constructor {
    double width, height, depth;

   
    no_arguments__constructor() {
        width = 10;
        height = 10;
        depth = 10;
    }

    double volume() {
        return width * height * depth;
    }

    public static void main(String args[]) {
        double vol;

       no_arguments__constructor mybox1 = new no_arguments__constructor();
       no_arguments__constructor mybox2 = new no_arguments__constructor();

        vol = mybox1.volume();
        System.out.println("Volume is: " + vol);

        vol = mybox2.volume();
        System.out.println("Volume is: " + vol);
    }
}
