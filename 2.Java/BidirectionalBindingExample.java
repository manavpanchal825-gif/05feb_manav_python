import javafx.beans.property.StringProperty;
import javafx.beans.property.SimpleStringProperty;

public class BidirectionalBindingExample 
{
    public static void main(String args[])
    {
        StringProperty propertyA = new SimpleStringProperty("HELLO");
        StringProperty propertyB = new SimpleStringProperty();
        
        propertyA.bindBidirectional(propertyB);
        
        propertyA.set("new value");
        System.out.println("propertyA:"+propertyA.get());
        System.out.println("propertyB:"+propertyB.get());
        
        propertyB.set("Another Value");
        System.out.println("propertyA:"+propertyA.get());
        System.out.println("propertyA:"+propertyB.get());
    }
}    
 