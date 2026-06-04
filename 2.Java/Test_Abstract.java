abstract class Shape 
{
    abstract void draw();
}

class RectangleApp extends Shape
{
    void draw()
    {
        System.out.println("drawing rectangle");
    }
}
class Circle extends Shape 
{
    void draw() 
    {
        System.out.println("drawing circle");
    }
}
public class Test_Abstract 
{
    public static void main(String[] args)
    {
        Shape s;
        s = new Circle();
        s.draw();
        s = new RectangleApp();
        s.draw();
    }
}

