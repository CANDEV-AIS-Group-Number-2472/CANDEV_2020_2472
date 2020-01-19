import java.io.BufferedReader;
import java.io.FileReader;
import java.util.List;
import java.util.ArrayList;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Arrays;

public class Validity2{

  public void valid  (String name) throws IOException{

    BufferedReader read = new BufferedReader(new FileReader(name));
    String line = read.readLine();
    ArrayList<String> validShips = new ArrayList<String>();
    ArrayList<String> invalidShips = new ArrayList<String>();

    while( (line = read.readLine())  != null){

      String[] values = line.split(",");
      if((values[14]).equals("NA") || Integer.parseInt((values[14])) == 0){
        System.out.println(" " + values[16] + " is not a valid ship: " + values[14] + " " );
        invalidShips.add(values[16]);


      }else if ( Integer.parseInt((values[14])) != 0){
        System.out.println(" " + values[16] + " is a valid ship: " + values[14] + " " );
        validShips.add(values[16]);
      }
    }

}



}
