import java.awt.BasicStroke;        
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;
import javax.swing.JFrame;

public class triangle extends JFrame implements ActionListener, MouseListener,MouseMotionListener {
 int xx[]= {20, 50, 80};
 int yy[]= {80, 30, 80};
Color clr;
int xm=0;
int ym=0;
int n=0;
 public triangle () {
     setTitle("zadacha2");
     setSize(1280,720);
     addMouseListener(this);
 }
 public static void main(String[] args) {
     //TODO code application logic here
     java.awt.EventQueue.invokeLater(new Runnable() {
           public void run() {
                triangle frame = new triangle();
                frame.setVisible(true);              
           }
     });
 }
 public void fillPolygon(int x, int y, int i) {
	
     Graphics g = this.getGraphics();
     Color clr = new Color((int) (Math.random() * 255),
			 (int) (Math.random() * 255), (int) (Math.random() *
			 255));
     g.setColor(clr);
     int[] fillx = {xx[0]+x,xx[1]+x,xx[2]+x};
     int[] filly = {yy[0]+y,yy[1]+y,yy[2]+y};
     
     g.fillPolygon(fillx, filly, i);

 }
 public void drawPolygon(int x, int y, int i)
 {
	 
     Graphics g = this.getGraphics();
     g.setColor(Color.BLACK);
     
     Graphics2D g2 = (Graphics2D) g;
     g2.setStroke(new BasicStroke(5));
     

     
     int[] drawx = {xx[0]+x,xx[1]+x,xx[2]+x};
     int[] drawy = {yy[0]+y,yy[1]+y,yy[2]+y};
     
     g.drawPolygon(drawx, drawy, i);

 }

 int x, y;

 @Override
 public void mouseClicked(MouseEvent e) {
	 
	 if (e.getButton()==MouseEvent.BUTTON1 && n<1) {
		 x = e.getX()-50;
	     y = e.getY()-55;
         n=n+1;
     drawPolygon(x,y,3);
     repaint();
	 }
	 if (e.getButton()==MouseEvent.BUTTON3) {

		 xm=e.getX();ym=e.getY();
		 if (xm>x+20 && xm<x+80 && ym>y+30 && ym<y+80)	 
			fillPolygon(x, y, 3);
		  repaint();
	 }
	 }
 @Override
 public void paint(Graphics g) {}
 public void mouseExited(MouseEvent e) {}
 public void mousePressed(MouseEvent e) {}
 public void mouseReleased(MouseEvent e) {}
 public void mouseEntered(MouseEvent e) {}
@Override
public void mouseDragged(MouseEvent e) {}
@Override
public void mouseMoved(MouseEvent e) {}
}
