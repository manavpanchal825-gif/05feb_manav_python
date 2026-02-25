import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.Stage;
import javafx.scene.paint.*;
import javafx.scene.text.*;
import javafx.geometry.*;
import javafx.scene.shape.*;

public class Font_1 extends Application
{
    public void start(Stage stage)
    {
        try
        {
            stage.setTitle("Font");
            TextFlow text_flow= new TextFlow();
            Text text_1 =new Text("GreeksForGreeks\n");
            text_1.setFill(Color.CYAN);
            Font font = Font.font("Verdana",FontWeight.EXTRA_BOLD,25);
            text_1.setFont(font);
            text_flow.getChildren().add(text_1);
            text_flow.setLineSpacing(20.0f);
            VBox vbox = new VBox(text_flow);
            vbox.setAlignment(Pos.CENTER);
            Scene scene =new Scene(vbox,400,300);
            stage.setScene(scene);
            stage.show();
        }
        catch(Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
    public static void main(String args[])
    {
        launch(args);
    }
   
}