import java.awt.Color;
import java.awt.Graphics; 
import java.io.BufferedReader;
import java.io.FileReader;
import javax.swing.JFrame;

public class zad1 extends JFrame 
{
	static int  n;
	static int fig[][]=new int[100][4];
      public zad1 ()
      {
             setTitle("zadacha1");
             setSize(920, 680);
             setVisible(true);
             setDefaultCloseOperation(EXIT_ON_CLOSE);
      }
      public static void readFromFile(){
    	  try {
  			BufferedReader in = new BufferedReader (new FileReader ("C:/Users/edisa/Desktop/zad1.txt")); //change this for your own pc
  			String line;	
  			line=in.readLine();n=Integer.parseInt(line);
  			//System.out.println(n);
  			for(int i=0;i<n;i++) {
  				line=in.readLine();
  				//System.out.println(line);
  				String[] vals=line.split(" ");
  				fig[i][0]=Integer.parseInt(vals[0]);
  				fig[i][1]=Integer.parseInt(vals[1]);
  				fig[i][2]=Integer.parseInt(vals[2]);
  				fig[i][3]=Integer.parseInt(vals[3]);
  			}			
  		} catch (Exception e) {e.printStackTrace();}
      }
      public void paint(Graphics g)
      { 
    	
    	  for(int i=0;i<n;i++) {
    		Color clr = new Color((int) (Math.random() * 255),
    					 (int) (Math.random() * 255), (int) (Math.random() *
    					 255));
    		g.setColor(clr);
    		  g.drawRect(fig[i][0],fig[i][1],fig[i][2]-fig[i][0],fig[i][3]-fig[i][1]);
    	  }
      }
      
       public static void main(String[] args)
       {  
    	   readFromFile();
    	   zad1 g = new zad1();
       }
}
