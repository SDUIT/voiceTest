import os
import drowSound
import imgDiff
from PIL import Image

def drowOrg( sound ) :

    path = sound.split("/")
    curSound = path[ len(path)-1 ];

    curImage = curSound[:-4]
    curSound = sound
    curImage = "images/org/" + curImage + ".png"
    if drowSound.drow( curSound, curImage ) == True :
        #print curSound + " " + curImage
           
        img = Image.open( curImage )
        area = (170, 48, 1352, 372)
        cropped_img = img.crop(area)
        cropped_img.save( curImage )
        return True
    else :
        return False
    
def drowRec( sound ) :

    path = sound.split("/")
    curSound = path[ len(path)-1 ];

    curImage = curSound[:-4]
    curSound = sound
    curImage = "images/rec/" + curImage + ".png"
    if drowSound.drow( curSound, curImage ) == True :
        #print curSound + " " + curImage
        
        img = Image.open( curImage )
        area = (170, 48, 1352, 372)
        cropped_img = img.crop(area)
        cropped_img.save( curImage )
        return True
    else :
        return False
        

def drowList( sound ) :

    path = sound.split("/")
    curSound = path[ len(path)-1 ];

    curImage = curSound[:-4]
    curSound = sound  
    curImage = "images/rec/" + curImage + ".png"
    drowSound.drow( curSound, curImage )
    #print curSound + " " + curImage

    img = Image.open( curImage )
    area = (170, 48, 1352, 372)
    cropped_img = img.crop(area)
    cropped_img.save( curImage )

def existOrg( x ):

    path = x.split('/')
    item = path[ len(path)-1 ]
    item = item[:-3] + "png"

    List = os.listdir("images/org")
    
    for i in List:
      if(i == item):
         return True
    return False  

def existRec( x ):

    path = x.split('/')
    item = path[ len(path)-1 ]
    item = item[:-3] + "png"

    List = os.listdir("images/rec")
    
    for i in List:
      if(i == item):
         return True
    return False  
    
def main(org, rec) :

    fr = True
    se = True
    if( existOrg(org) == False ):
        fr = drowOrg(org)
        
    if( existRec(rec) == False ):
        se = drowRec(rec)
        
    #os.remove(org)    
    #os.remove(rec)
    
    if fr == True and se == True :
        org = org.split("/")
        org = org [ len(org) -1 ]
        org = org[:-4]
        org = "images/org/" + org + ".png"
        
        rec = rec.split("/")
        rec = rec [ len(rec) -1 ]
        rec = rec [:-4]
        rec = "images/rec/" + rec + ".png"
            
        return imgDiff.main(org,rec)

    else :
        return "Image Size Error!"  
