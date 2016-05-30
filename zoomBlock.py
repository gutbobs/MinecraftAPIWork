#!/usr/bin/env python
import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.postToChat("Hello world")



def zoomBlockX(x,y,z,blockType,zoomRange):
	for i in range(zoomRange):
		mc.setBlock(x+i,y,z,blockType)
		mc.setBlock(x+i-1,y,z,0)
		time.sleep(0.01)
		
def zoomBlockZ(x,y,z,blockType,zoomRange):
	for i in range(zoomRange):
		mc.setBlock(x,y,z+i,blockType)
		mc.setBlock(x,y,z+i-1,0)
		time.sleep(0.01)	

def zoomBlockY(x,y,z,blockType,zoomRange):
	for i in range(zoomRange):
		mc.setBlock(x,y+i,z,blockType)
		mc.setBlock(x,y+i-1,z,0)
		time.sleep(0.01)			
