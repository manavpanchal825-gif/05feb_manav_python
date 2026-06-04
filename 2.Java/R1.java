import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;
public class R1 extends Application
{
    public void start(Stage stage)
    {
       Rectangle rectangle = new Rectangle();
        rectangle.setX(100);
        rectangle.setY(100);
        rectangle.setWidth(60);
        
        rectangle.setHeight(60);
        rectangle.setFill(Color.LIGHTBLUE);
        rectangle.setStroke(Color.DARKBLUE);
        rectangle.setStrokeWidth(60);
        
        Pane root =new Pane();
        root.getChildren().add(rectangle);
        Scene scene =new Scene(root,400,300);
        stage.setTitle("javafx Rectange Example");
        stage.setScene(scene);
        stage.show();
       
    }        
    public static void main(String args[])
    {
        launch(args);
    }
 }