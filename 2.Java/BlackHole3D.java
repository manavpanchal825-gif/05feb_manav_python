import javafx.animation.Animation;
import javafx.animation.KeyFrame;
import javafx.animation.KeyValue;
import javafx.animation.Timeline;
import javafx.application.Application;
import javafx.scene.*;
import javafx.scene.paint.Color;
import javafx.scene.paint.PhongMaterial;
import javafx.scene.shape.Box;
import javafx.scene.shape.Sphere;
import javafx.scene.transform.Rotate;
import javafx.stage.Stage;
import javafx.util.Duration;

public class BlackHole3D extends Application {

    @Override
    public void start(Stage stage) {
        // Create Black Hole
        Sphere blackHole = new Sphere(60);
        PhongMaterial mat = new PhongMaterial();
        mat.setDiffuseColor(Color.BLACK);
        blackHole.setMaterial(mat);

        // Create rotating ring (using many boxes)
        Group ring = new Group();
        for (int i = 0; i < 36; i++) {
            Box piece = new Box(10, 10, 60);
            piece.setMaterial(new PhongMaterial(Color.DARKGRAY));
            piece.setTranslateX(120);
            piece.setRotate(i * 10);
            ring.getChildren().add(piece);
        }

        // Group everything
        Group root = new Group(blackHole, ring);

        // Setup lighting
        AmbientLight light = new AmbientLight(Color.rgb(80, 80, 80));
        PointLight pointLight = new PointLight(Color.WHITE);
        pointLight.setTranslateZ(-300);
        root.getChildren().addAll(light, pointLight);

        // Setup camera
        PerspectiveCamera camera = new PerspectiveCamera(true);
        camera.setTranslateZ(-500);
        camera.setTranslateY(-40);
        camera.setNearClip(0.1);
        camera.setFarClip(2000.0);

        SubScene subScene = new SubScene(root, 800, 600, true, SceneAntialiasing.BALANCED);
        subScene.setCamera(camera);

        Scene scene = new Scene(new Group(subScene));
        stage.setTitle("Black Hole 3D Animation");
        stage.setScene(scene);
        stage.show();

        // Animation: rotate ring
        Rotate rotate = new Rotate(0, Rotate.Y_AXIS);
        ring.getTransforms().add(rotate);

        Timeline timeline = new Timeline(
            new KeyFrame(Duration.seconds(0),
                new KeyValue(rotate.angleProperty(), 0)),
            new KeyFrame(Duration.seconds(8),
                new KeyValue(rotate.angleProperty(), 360))
        );
        timeline.setCycleCount(Animation.INDEFINITE);
        timeline.play();
    }

    public static void main(String[] args) {
        launch(args);
    }
}