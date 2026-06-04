public class constructor_overloding {
    int id, age;
    String name;
    constructor_overloding() {
        id = 0;
        name = "";
        age = 0;
    }
    constructor_overloding(int i, String n) {
        id = i;
        name = n;
        age = 18;
    }
    constructor_overloding(int i, String n, int a) {
        id = i;
        name = n;
        age = a;
    }

    void display() {
        System.out.println(id + ""+ name+ ""+age);
    }

    public static void main(String args[]) {
        constructor_overloding s1= new constructor_overloding(1,"pm");
        constructor_overloding s2= new constructor_overloding(2,"pm",25);
        constructor_overloding s3= new constructor_overloding();

        s1.display();
        s2.display();
        s3.display();
    }
}
