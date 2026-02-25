public class advantages_of_static {
    int rollno;
    String name;
    static String college = "SVD";

    advantages_of_static(int r, String n) {
        rollno = r;
        name = n;
    }

    void display() {
        System.out.println(rollno + " " + name + " " + college);
    }

    public static void main(String args[]) {
        advantages_of_static s1 = new advantages_of_static(1, "Manav");
        advantages_of_static s2 = new advantages_of_static(2, "MANAV");

        s1.display();
        s2.display();
    }
}
