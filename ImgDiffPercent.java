
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import java.util.ArrayList;
import java.util.List;


public enum ImgDiffPercent {
    ;

    public static void main(String[] args) throws IOException {
        // https://rosettacode.org/mw/images/3/3c/Lenna50.jpg
        // https://rosettacode.org/mw/images/b/b6/Lenna100.jpg
        String x = "images/org/in.png";
		String y = "images/rec/1510483138.97-in.png";
		
		BufferedImage img1 = ImageIO.read(new File(x));
		BufferedImage img2 = ImageIO.read(new File(y));
		
		getDifferencePercent(img1 , img2 );
		/*
		List<String> in = new ArrayList<String>();

		
		File[] files = new File("images/rec").listFiles();
		//If this pathname does not denote a directory, then listFiles() returns null. 

		for (File file : files) {
			if (file.isFile() && !file.getName().equals("Thumbs.db") ) {
				
				String y = "images/rec/" +file.getName() ; 
			    System.out.println( x + " " + y );
				BufferedImage img2 = ImageIO.read(new File(y));
		
				getDifferencePercent(img1 , img2 );
			}
		}
		*/
		
		
	}

    private static double getDifferencePercent(BufferedImage img1, BufferedImage img2) {
        int width = img1.getWidth();
        int height = img1.getHeight();
        int width2 = img2.getWidth();
        int height2 = img2.getHeight();
        if (width != width2 || height != height2) {
            throw new IllegalArgumentException(String.format("Images must have the same dimensions: (%d,%d) vs. (%d,%d)", width, height, width2, height2));
        }
		System.out.println(width + " " + height);
        long diff = 0;
        int k = 0;
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                int color = img1.getRGB(x,y);
                int b = color & 0xff;
                int g = (color & 0xff00) >> 8;
                int r = (color & 0xff0000) >> 16;

                int color2 = img2.getRGB(x,y);
                int b2 = color & 0xff;
                int g2 = (color & 0xff00) >> 8;
                int r2 = (color & 0xff0000) >> 16;

                if( r==0 && g==0 && b==0 && r2==0 && g2==0 && b2==0  ) {
                    k++;
                }

                else if( r==255 && g==255 && b==255 && r2==255 && g2==255 && b2==255  ) {
                    k++;
                }

                ///System.out.println( r + " " + g + " " + b );
                //System.out.println( pixelDiff(img1.getRGB(x, y), img2.getRGB(x, y)) );
				
				diff += pixelDiff(img1.getRGB(x, y), img2.getRGB(x, y));
                
			}
        }
        long maxDiff = 3L * 255 * (width * height-k);

        System.out.println("***************************************************************");
		//System.out.println("\n");
		//System.out.println("Test Result:");
		//System.out.println( "There is " + height*width + " pixel in image" );
		//System.out.println( "There is " + k + " Black and White pixel in image" );
		//System.out.println( "We checked Only " + ( height*width - k) + " pixel for Difference" );
		//System.out.println( "Max Diff can be " + maxDiff + " pixel in image" );
		//System.out.println( "I Found " + diff + " different pixel in image" );
		double p =  100.0 * diff / maxDiff;
    
        System.out.println("So Diff percent is: " + p);
        //System.out.println("\n");
		System.out.println("***************************************************************");
		
		return 1.0;		
	}

    private static int pixelDiff(int rgb1, int rgb2) {
        int r1 = (rgb1 >> 16) & 0xff;
        int g1 = (rgb1 >>  8) & 0xff;
        int b1 =  rgb1        & 0xff;
        int r2 = (rgb2 >> 16) & 0xff;
        int g2 = (rgb2 >>  8) & 0xff;
        int b2 =  rgb2        & 0xff;
        return Math.abs(r1 - r2) + Math.abs(g1 - g2) + Math.abs(b1 - b2);
    }
}
