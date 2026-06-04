import javafx.animation.FadeTransition;
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;
import javafx.util.Duration;

public class FadeTrasitiionExample extends Application {

    @Override
    public void start(Stage stage) {
        Button button = new Button("Click Me");
        button.setOnAction(new javafx.event.EventHandler<javafx.event.ActionEvent>()
        {
            public void handle(javafx.event.ActionEvent event)
            {
                System.out.println("BUTTON CLICKED");
            }
        });

        FadeTransition fade = new FadeTransition(Duration.seconds(2), button);
        fade.setFromValue(1.0);   
        fade.setToValue(0.0);     
        fade.setCycleCount(2);    
        fade.setAutoReverse(true);
        button.setOnAction(e -> fade.play());
        

        StackPane root = new StackPane(button);
        Scene scene = new Scene(root, 400, 300);

        stage.setTitle("JavaFX Fade Transition Example");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}