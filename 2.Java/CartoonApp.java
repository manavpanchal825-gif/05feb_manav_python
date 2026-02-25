import javafx.animation.Animation;
import javafx.animation.TranslateTransition;
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.Group;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;
import javafx.util.Duration;

public class CartoonApp extends Application {

    @Override
    public void start(Stage stage) {

        // Background
        Rectangle sky = new Rectangle(800, 600);
        sky.setFill(Color.SKYBLUE);

        // Sun
        Circle sun = new Circle(50);
        sun.setFill(Color.YELLOW);
        sun.setTranslateX(700);
        sun.setTranslateY(100);

        // Ground
        Rectangle ground = new Rectangle(800, 200);
        ground.setFill(Color.GREEN);
        ground.setTranslateY(400);

        // Simple Character (Ball)
        Circle character = new Circle(30);
        character.setFill(Color.RED);
        character.setTranslateX(100);
        character.setTranslateY(370);

        Group root = new Group(sky, sun, ground, character);

        Scene scene = new Scene(root, 800, 600);

        stage.setTitle("Simple Cartoon Animation");
        stage.setScene(scene);
        stage.show();

        // Animation (Moving Character)
        TranslateTransition move = new TranslateTransition();
        move.setDuration(Duration.seconds(5));
        move.setNode(character);
        move.setFromX(0);
        move.setToX(600);
        move.setCycleCount(Animation.INDEFINITE);
        move.setAutoReverse(true);
        move.play();
    }

    public static void main(String[] args) {
        launch();
    }
}