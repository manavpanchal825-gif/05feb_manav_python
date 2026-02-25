import java.util.Scanner;

public class scannerclass {
    public static void main(String args[]) {

        Scanner myobj = new Scanner(System.in);
        System.out.println("Enter name, age and salary:");
        String name = myobj.nextLine();
        int age = myobj.nextInt();
        double salary = myobj.nextDouble();
        System.out.println("Name: " +name);
        System.out.println("Age: " + age);
        System.out.println("Salary: " + salary);
        myobj.close();
    }
}
