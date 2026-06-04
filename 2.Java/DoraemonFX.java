import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.Group;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.scene.shape.Line;
import javafx.stage.Stage;

public class DoraemonFX extends Application {

    @Override
    public void start(Stage stage) {

        Circle face = new Circle(200, 200, 150);
        face.setFill(Color.DODGERBLUE);

        Circle whiteFace = new Circle(200, 230, 120);
        whiteFace.setFill(Color.WHITE);

        Circle leftEye = new Circle(170, 150, 30);
        leftEye.setFill(Color.WHITE);

        Circle leftPupil = new Circle(170, 160, 10);
        leftPupil.setFill(Color.BLACK);

        Circle rightEye = new Circle(230, 150, 30);
        rightEye.setFill(Color.WHITE);

        Circle rightPupil = new Circle(230, 160, 10);
        rightPupil.setFill(Color.BLACK);
      
        Circle nose = new Circle(200, 190, 15);
        nose.setFill(Color.RED);

        Line mouth = new Line(160, 260, 240, 260);

        Group root = new Group(face, whiteFace,
                leftEye, leftPupil,
                rightEye, rightPupil,
                nose, mouth);

        Scene scene = new Scene(root, 400, 400);

        stage.setTitle("Simple Doraemon - JavaFX");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}