"""
Created on Wed Jan 30 00:21:00 2019

@author: hannakristensen
"""

import os
import re

#this function helps make a circle
def spiral():
	x = 0
	y = 0
	d = 1
	m = 1
	listX = []
	listY = []
	for i in range(0, 10):
		while((2 * x * d) < m):
			listX.append(x)
			listY.append(y)
			x = x + d
		while((2 * y * d) < m):
			listX.append(x)
			listY.append(y)
			y = y + d
		d = -1 * d
		m = m + 1
	
	return listX, listY
#return the two lists with x and y cordinates in them

fin = open( 'base.pov' )
sdl = fin.read()
fin.close()

#regular expression for camera
findStr = r"camera\s*{\s*location\s*<\s*\-*\d+,\-*\d+,\-*\d+\s*>"
#set up the lists for x, y, and z cordinates
listOfX, listOfY = spiral()
listOfZ = range(0, 50)
print(listOfX)
num = 0

#for loop for making the movie, the if statment helps slow down the helix a bit
for i in range(0, 47):
        sdl = re.sub( findStr , "camera{location<" + str(listOfX[num] / 4) + ',' + str(listOfZ[num] / 7) + ',' + str(listOfY[num] / 4) + ">" , sdl )
        if i%2 == 0:
                sdl = re.sub( findStr , "camera{location<" + str(listOfX[num] / 3) + ',' + str(listOfZ[num] / 7) + ',' + str(listOfY[num] / 3) + ">" , sdl )
                num = num + 1

        outfile = 'temp.pov'
        fout = open(outfile,'w')
        fout.write(sdl)
        fout.close()

        pov_cmd = "pvengine.exe +I%s +O%s -D -V +A +H600 +W800 /exit"
        cmd = pov_cmd % ('temp.pov', "temp" + str(i).zfill(4) + ".png")
        os.system(cmd)
	
print('Encoding movie')
os.system('mencoder.exe mf://temp*.png -mf type=png:fps=25 -ovc lavc -lavcopts vcodec=msmpeg4:vbitrate=2160000:keyint=5:vhq -o movie.avi')




