import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.stage.Stage;

public class CIRCLE extends Application
{
    @Override
    public void start(Stage stage)
    {
        Circle circle = new Circle();
        circle.setCenterX(100);
        circle.setCenterY(100);
        circle.setRadius(50);
        circle.setFill(Color.LIGHTBLUE);
        circle.setStroke(Color.DARKBLUE);
        circle.setStrokeWidth(2);

        Pane root = new Pane();
        root.getChildren().add(circle);

        Scene scene = new Scene(root, 400, 300);
        stage.setTitle("JavaFX Circle Example");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args)
    {
        launch(args);
    }
}
