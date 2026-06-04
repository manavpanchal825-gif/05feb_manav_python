public class FinalKeyword {

    final void run() {
        System.out.println("running");
    }

    public static void main(String[] args) {
        FinalKeyword obj = new FinalKeyword();
        obj.run();
    }
}
