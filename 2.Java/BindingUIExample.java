import javafx.application.Application;
import javafx.beans.property.StringProperty;
import javafx.beans.property.SimpleStringProperty;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

public class BindingUIExample extends Application
{
    public void start(Stage primaryStage)
    {
        StringProperty textProperty= new SimpleStringProperty("hello,javafx!");
        Label label= new Label();
        
        label.textProperty().bind(textProperty);
        
        StackPane root = new StackPane();
        root.getChildren().add(label);
        
        Scene scene=new Scene(root,300,250);
        primaryStage.setTitle("Property Binding Example");
        primaryStage.setScene(scene);
        primaryStage.show();
        new Thread(()->
        {
        try
        {
            Thread.sleep(2000);
            textProperty.set("Update text");
        }
        catch(InterruptedException e)
        {
            e.printStackTrace();
        }
    }).start();
}
public static void main(String args[])
{
    launch(args);
}
}