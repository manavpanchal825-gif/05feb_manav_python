import javafx.animation.KeyFrame;
import javafx.animation.Timeline;
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.stage.Stage;
import javafx.util.Duration;

public class AnimationDemo extends Application {

    double dx = 3; 
    @Override
    public void start(Stage stage) {

        Pane pane = new Pane();

        Circle circle = new Circle(30);
        circle.setFill(Color.BLUE);
        circle.setCenterX(50);
        circle.setCenterY(150);

        pane.getChildren().add(circle);

        Timeline animation = new Timeline(
            new KeyFrame(Duration.millis(20), e -> {

                circle.setCenterX(circle.getCenterX() + dx);

                if (circle.getCenterX() > 470 || circle.getCenterX() < 30) {
                    dx = -dx;
                }
            })
        );

        animation.setCycleCount(Timeline.INDEFINITE);
        animation.play();

        Scene scene = new Scene(pane, 500, 300);
        stage.setTitle("JavaFX Animation Example");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}