import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

public class JavaFXDemo extends Application 
{
    public void start(Stage primaryStage) 
    {
        Button btn = new Button("CLICK ME");
        StackPane root= new StackPane(btn);
        Scene scene= new Scene(root,300,200);
        primaryStage.setTitle("JAVAFX BASIC STRUCTURE");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
    public static void main(String args[])
    {
        launch(args);
    }
}