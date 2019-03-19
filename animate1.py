"""
Created on Wed Jan 30 00:21:00 2019

@author: hannakristensen
"""

import os
import re
import spiral
#class box with a constructor and a function to return a string of the object
class Box:
    def __init__(self ,position, color):
        self.color = color
        self.position = position
    
    def string(objectPrint):
        return str('box { <-1.00, 0.00, -1.00>,< 1.00, 2.00, 1.00> {texture { pigment { color rgb' + str(objectPrint.color) + '} finish { phong 1 reflection{ 0.00 metallic 0.00} } } scale <1,1,1> rotate<0,0,0> translate' + str(objectPrint.position) + '}')
    def changePosition(positionBox, positionChange):
        positionBox.position = positionChange

    



fin = open( 'base.pov' )
sdl = fin.read()
fin.close()

#regular expression for camera
findStr = r"camera\s*{\s*location\s*<\s*\-*\d+,\-*\d+,\-*\d+\s*>"
listForCam = range(0, 10)

#lists for x, y, and z cordinates
listOfX, listOfY = spiral.spiral()
listOfZ = range(0, 50)
num = 1
#in this for loop we change the camera a bit
for i in range(0, 10):
    #finding and changing in sdl the camera line
    if i%2 == 0:
        sdl = re.sub( findStr , "camera{location < " + str(0) + ' , ' + str(listForCam[num]) + ' , ' + str(-7) + " >" , sdl )
        num = num + 1

    outfile = 'temp.pov'
    fout = open(outfile,'w')
    fout.write(sdl)
    fout.close()
	
    pov_cmd = "pvengine.exe +I%s +O%s -D -V +A +H600 +W800 /exit"
    cmd = pov_cmd % ('temp.pov', "temp" + str(i).zfill(4) + ".png")
    os.system(cmd)
#made a box object passed as keyword arguments
newBox = Box('<2,2,2>', '<66,78,244>')
#set camera in a position before for loop
sdl = sdl + 'camera {location<0,7,-7> look_at < 0 , 0 , 0 >}'

#in this for loop it moves the box and changes its color
for i in range(0, 100):
    #add in the box boject
    newSdl = sdl + str('box { <-1.00, 0.00, -1.00>,< 1.00, 2.00, 1.00> texture { pigment { color rgb' + str(newBox.color) + '} finish { phong 1 reflection{ 0.00 metallic 0.00} } } scale <1,1,1> rotate<0,0,0> translate' + str(newBox.position) + '}')
    #chnage the box object position but only for a little, keyword arguments used
    if i < 6:
        newBox.changePosition(positionBox = newBox,  positionChange = str('<' + str(listOfZ[i]) + ',' + str(listOfZ[i]) + ',' + str(listOfZ[i]) + '>'))
    #change its color every once in a while
    if i%6 == 0:
        newBox.color = str('<' + str(listOfY[i] * 2) + ',' + str(listOfY[i] * 3) + ',' + str(listOfX[i] * 2) + '>')
    #set the box in a position after it has moved around
    if i == 7:
        newBox.position = str('<' + str(1) + ',' + str(1) + ',' + str(1) + '>')
    
    outfile = 'temp.pov'
    fout = open(outfile,'w')
    fout.write(newSdl)
    fout.close()
    
    pov_cmd = "pvengine.exe +I%s +O%s -D -V +A +H600 +W800 /exit"
    cmd = pov_cmd % ('temp.pov', "temp" + str(i + 10).zfill(4) + ".png")
    os.system(cmd)	
    
print('Encoding movie')
os.system('mencoder.exe mf://temp*.png -mf type=png:fps=25 -ovc lavc -lavcopts vcodec=msmpeg4:vbitrate=2160000:keyint=5:vhq -o movie(1).avi')


