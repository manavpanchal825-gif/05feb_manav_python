import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;

public class ImageClass extends Application
{
    public void start(Stage primaryStage)
    {
        Image image = new Image("file:D:\\neenu\\bca4_manav\\src\\download.jpg");
        
        ImageView imageview = new ImageView(image);
        
        imageview.setFitWidth(300);
        imageview.setFitHeight(200);
        imageview.setPreserveRatio(true);
        
        StackPane root = new StackPane();
        root.getChildren().add(imageview);
        Scene scene = new Scene(root,400,300);
        
        primaryStage.setTitle("ImageView Example");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
    public static void main(String args[])
    {
        launch(args);
    }
}    

