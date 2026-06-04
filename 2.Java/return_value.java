public class return_value {
    double width, height, depth;

    double volume() {
        return width * height * depth;
    }

    public static void main(String args[]) {
        return_value mybox1 = new return_value();
        return_value mybox2 = new return_value();
        double vol;

        mybox1.width = 10;
        mybox1.height = 15;
        mybox1.depth = 20;

        mybox2.width = 2;
        mybox2.height = 3;
        mybox2.depth = 5;

        vol = mybox1.volume();
        System.out.println("Volume is: " + vol);

        vol = mybox2.volume();
        System.out.println("Volume is: " + vol);
    }
}
