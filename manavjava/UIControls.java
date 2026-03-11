import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.media.*;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import java.io.File;

public class UIControls extends Application 
{

    @Override
    public void start(Stage primaryStage)
    {
        primaryStage.setTitle("JAVA FX CONTROLS DEMO");
        Label label = new Label("ENTER YOUR DETAILS:");
        
        TextField textfield = new TextField();
        textfield.setPromptText("Name");
        TextArea textarea = new TextArea();
        textarea.setPromptText("Enter Address");
        
        CheckBox checkbox = new CheckBox("Subscribe To Newsletter");
        
        ToggleGroup gendergroup = new ToggleGroup();
        RadioButton maleradiobutton = new RadioButton("MALE");
        RadioButton femaleradiobutton = new RadioButton("FEMALE");
        maleradiobutton.setToggleGroup(gendergroup);
        femaleradiobutton.setToggleGroup(gendergroup);
       
        ComboBox<String> combobox = new ComboBox<>();
        combobox.getItems().addAll("Student","Teacher","Admin");
        combobox.setPromptText("Select Role");
       
        ListView<String> listview = new ListView<>();
        listview.getItems().addAll("Java","Python","C++","C#");
        listview.setPrefHeight(100);
       
        ScrollBar scrollbar = new ScrollBar();
        scrollbar.setMin(0);
        scrollbar.setMax(100);
       
        Slider slider = new Slider(0,100,50);
       
        Button submitbutton = new Button("SUBMIT");
       
        Media vd = new Media(new File("D:\\neenu\\bca4_manav\\Vedio2.mp4").toURI().toString());
        MediaPlayer videoplayer = new MediaPlayer(vd);
        MediaView mediaview = new MediaView(videoplayer);
        mediaview.setFitHeight(300);
        mediaview.setFitWidth(300);
        videoplayer.play();
      
        VBox layout = new VBox(10);
        layout.getChildren().addAll( label,textfield,textarea, checkbox, maleradiobutton,femaleradiobutton,combobox,listview,scrollbar,slider,submitbutton,mediaview);

        Scene scene = new Scene(layout, 400, 600);

        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) 
    {
        launch(args);
    }
}