import os
import math

from PIL import Image

def pixelDiff(rgb , rgb2 ):
    
    return math.fabs( rgb[0] - rgb2[0] ) +  math.fabs( rgb[1] - rgb2[1] ) + math.fabs( rgb[2] - rgb2[2] )

def getDiffPercent(path, path2 ):
    """Get a numpy array of an image so that one can access values[x][y]."""
    global ans
    ans = []
    img = Image.open( path )    
    img2 = Image.open( path2 )

    width, height = img.size
    width2, height2 = img2.size
            
    diff = 0
    k = 0

    for i in range(width):  
      for j in range(height):
        rgb = img.load()[i,j]
        rgb2 = img2.load()[i,j]
        
        if( rgb[0] == rgb2[0] and rgb[1] == rgb2[1] and rgb[2] == rgb2[2] and rgb[0] == 0 and rgb[1] == 0 and rgb[2] == 0 ):
            k = k+1
        if( rgb[0] == rgb2[0] and rgb[1] == rgb2[1] and rgb[2] == rgb2[2] and rgb[0] == 255 and rgb[1] == 255 and rgb[2] == 255 ):
            k = k+1    
        
        diff = diff + pixelDiff(rgb, rgb2)

    img.close()
    img2.close()
    
    mx = 3 * 255 * ( width * height - k)
    return 100*diff/mx    

def main(org, rec):
        
    ans = getDiffPercent( org, rec )
    #os.remove(rec)
    return ans
