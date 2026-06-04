import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Ellipse;
import javafx.stage.Stage;

public class exellips extends Application 
{
    public void start(Stage stage)
    {
        Ellipse ellipse = new Ellipse();
        ellipse.setCenterX(150);
        ellipse.setCenterY(150);
        ellipse.setRadiusX(100);
        ellipse.setRadiusY(50);
        ellipse.setFill(Color.LIGHTBLUE);
        ellipse.setFill(Color.AQUA);
        ellipse.setStroke(Color.DARKGRAY);
        Pane root =new Pane();
        root.getChildren().add(ellipse);
        
        Scene scene =new Scene(root,300,400);
        stage.setTitle("Javafx Ellipse Example");
        stage.setScene(scene);
        stage.show();
        
    }
    public static void main(String args[])
    {
        launch(args);
    }
}    
 