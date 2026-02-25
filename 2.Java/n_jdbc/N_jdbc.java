    /*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package n_jdbc;

/**
 *
 * @author Admin
 */
import java.sql.*;
import java.sql.PreparedStatement;
import java.util.Scanner;
import static java.lang.System.exit;
public class N_jdbc {
   static final String url = "jdbc:mysql://localhost:3306/employeedb";
public static void createData()
{
        final String uname = "root";
        final String pass = "";
        Scanner sc = new Scanner(System.in);
        System.out.print("\tEnter employee ID number : ");
        int id = sc.nextInt();
        System.out.print("\tEnter employee name : ");
        String name = sc.next();
        System.out.print("\tEnter employee department : ");
        String department = sc.next();
        System.out.print("\tEnter employee Location : ");
        String location = sc.next();

        String query="INSERT INTO employee (id, name, department, location) values ('"+id+"','"+name+"','"+department+"','"+location+"')";
        Connection con;
        try{
            con=DriverManager.getConnection(url,uname,pass);
            PreparedStatement stmt = con.prepareStatement(query);
            int rows = stmt.executeUpdate(query);
            
	    if(rows==1) {
                System.out.println("\t\t DONE");
            }else {
                System.out.println("\t\tError");
            }
            menu();
        }catch (Exception e){
            e.printStackTrace();
        }
    }
    public static void readData(){
        final String uname = "root";
        final String pass = "";
        String query = "select * from employee";
        Connection con;
        try {
            con = DriverManager.getConnection(url, uname, pass);
            Statement st = con.createStatement();
            ResultSet rs = st.executeQuery(query);
            
	    while(rs.next()) {
                int id = rs.getInt("id");
                String name = rs.getString("name");
                String department = rs.getString("department");
                String location = rs.getString("location");

                System.out.println("\tEmp ID : "+id+"  Name -->> "+name+"    Department -->> "+department+"    Location -->> "+location);
            }
            menu();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    public static void deleteData(){
        final String uname = "root";
        final String pass = "";
        System.out.print("\tEnter Employee ID number : ");
        Scanner sc = new Scanner(System.in);
        int id = sc.nextInt();
        String query = "DELETE  FROM employee where id ='"+id+"' ";

        Connection con;
        try{
            con = DriverManager.getConnection(url,uname,pass);
            PreparedStatement stmt = con.prepareStatement(query);
            int rows = stmt.executeUpdate(query);
	    if(rows==1) {
                System.out.println("\t\t DONE");
            }else {
                System.out.println("\t\tPlease enter correct ID number!!!! ");
                deleteData();
            }
            menu();
        }catch (Exception e){
            e.printStackTrace();
        }
    }
    public static void updateData(){
        final String uname = "root";
        final String pass = "";
        String query = null;
        Scanner sc = new Scanner(System.in);
        System.out.println("\t1 - ID no. Updates");
        System.out.println("\t2 - Name Updates");
        System.out.println("\t3 - Location Updates");
        System.out.println("\t4 - Department Updates");
        System.out.print("\t\t Choose Option to Updates data -->> ");
        int opt = sc.nextInt();
        if(opt==1){
            System.out.print("\n\tEnter name of Employee : ");
            String name = sc.next();
            System.out.print("\tEnter to updates ID number : ");
            int id = sc.nextInt();
            query = "UPDATE employee SET id ='"+id+"' where name ='"+name+"' ";
        
	}else if(opt==2){
            System.out.print("\n\tEnter employee ID number : ");
            int id = sc.nextInt();
            System.out.print("\tEnter Names to Updates  : ");
            String name = sc.next();
            query = "UPDATE employee SET name ='"+name+"' where id ='"+id+"' ";
        
	}else if(opt==3){
            System.out.print("\n\tEnter employee ID number : ");
            int id = sc.nextInt();
            System.out.print("\tEnter Location to updates  : ");
            String location = sc.next();
            query = "UPDATE employee SET location ='"+location+"' where id ='"+id+"' ";
        }else if(opt==4){
            System.out.print("\n\tEnter employee ID number : ");
            int id = sc.nextInt();
            System.out.print("\tEnter Department Names to Updates  : ");
            String department = sc.next();
            query = "UPDATE employee SET department ='"+department+"' where id ='"+id+"' ";
        }
        else {
            System.out.println("\n\tChoose correct option ......");
            updateData();
        }
        Connection con;
        
	try{
            con = DriverManager.getConnection(url,uname,pass);
            PreparedStatement stmt = con.prepareStatement(query);
            int rows = stmt.executeUpdate(query);
            if(rows==1) {
                System.out.println("\t\t DONE");
            }else {
                System.out.println("\t\tPlease enter correct data .....!! ");
                updateData();
            }
            menu();
        }catch (Exception e){
            e.printStackTrace();
        }
    }
    public static void menu() {
        System.out.println("\n\n\t OPERATIONS.....\n");
        System.out.println("\t1 - Create Data ");
        System.out.println("\t2 - Read Data ");
        System.out.println("\t3 - Update Data ");
        System.out.println("\t4 - Delete Data ");
        System.out.println("\t5 - Exit");
        System.out.print("\t Select Option  ---->>>  ");
        Scanner sc = new Scanner(System.in);
        int select= sc.nextInt();
        switch (select) {
            case 1 : 
                System.out.println("\n\n\t Enter Employee Data\n");
                createData();
            case 2 :
                System.out.println("\n\n\t\t DATA \n");
                readData();
            case 3 :
                System.out.println("\n\n\t\t  Updates Employee Data \n");
                updateData();
            case 4 :
                System.out.println("\n\n\t\t Delete Employee Data \n");
                deleteData();
            case 5 :
                System.out.println("\t\t   Exiting....\n \t\t\t\t\t Thank You....");
                exit(0);
            default :
                System.out.println("Wrong Option...!");
                menu();   
        }
    }
    public static void main(String[] args) {
         menu();
    }
}

