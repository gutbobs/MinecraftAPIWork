#!/usr/bin/env python
print "Importing modules"
import sys
import time
from mcpi.minecraft import Minecraft
import numpy as np

from PIL import Image

def rgb2grey(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

def selectBlock(pixel):
	pixel=int(pixel)
	white=80
	midgrey1=42
	midgrey2=16
	midgrey3=98
	black=49
	if pixel==None: return black
	if 0 <= pixel <= 25: return black
	if 26 <= pixel <= 75: return midgrey3
	if 76 <= pixel <= 150: return midgrey2
	if 151 <= pixel <= 225: return midgrey1
	if 226 <= pixel <= 255: return white

	
inputfilename=sys.argv[1]
print "opening:",inputfilename
img = Image.open(inputfilename)
size=100,100
img.thumbnail(size,Image.ANTIALIAS)

print "loading to array"
arr = np.array(img)
print "connecting to Minecraft"

mc = Minecraft.create()
mc.postToChat("Starting")

blockType=3
x,y,z=mc.player.getPos()

rowcount=0
arrlen=len(arr)




print "iterating through image"
blockdict={}
for row in arr: 
	targetz=(arrlen-rowcount)+z
	colcount=0
	for col in row[::-1]:
		targetx=x+colcount
		pixel= selectBlock(rgb2grey(arr[rowcount,colcount]))
		#print arr[rowcount,colcount],pixel
		if blockdict.has_key(pixel): blockdict[pixel]+=1
		else: blockdict[pixel]=1
		mc.setBlock(targetx,y,targetz,pixel)
		colcount+=1
	rowcount+=1
mc.postToChat("Finished")