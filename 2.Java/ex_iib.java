public class ex_iib {
    int number;
    {
        System.out.println("Instance initialization block executed");
        number = 10;
    }
    public ex_iib() {
        System.out.println("Constructor 1 executed, number: " + number);
    }
    
    public ex_iib(int num) {
        System.out.println("Constructor 2 executed, number: " + number);
        this.number = num;
    }

    public static void main(String args[]) {
        new ex_iib();
        System.out.println("---");
        new ex_iib(20);
    }
}
