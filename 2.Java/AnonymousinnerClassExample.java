import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

public class AnonymousinnerClassExample extends Application 
{
    public void start(Stage primaryStage)
    {
        Button button =new Button("CLICK ME");
        button.setOnAction(new javafx.event.EventHandler<javafx.event.ActionEvent>()
        {
            public void handle(javafx.event.ActionEvent event)
            {
                System.out.println("BUTTON CLICKED");
            }
        });
        StackPane root = new StackPane(button);
        Scene scene =new Scene(root,300,400);
        
        primaryStage.setTitle("Anonymous Inner Class Example");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
    public static void main(String args[])
    {
        launch(args);
    }
}    
  