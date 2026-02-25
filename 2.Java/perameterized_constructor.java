public class perameterized_constructor{
    double width, height, depth;
    perameterized_constructor(double w, double h, double d) {
        width = w;
        height = h;
        depth = d;
    }

    double volume() {
        return width * height * depth;
    }

    public static void main(String args[]) {
        double vol;

        perameterized_constructor mybox1 =new perameterized_constructor(10, 20, 15);
        perameterized_constructor mybox2 =new perameterized_constructor(2, 3, 5);

        vol = mybox1.volume();
        System.out.println("Volume is: " + vol);

        vol = mybox2.volume();
        System.out.println("Volume is: " + vol);
    }
}
