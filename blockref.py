#!/usr/bin/env python
print "Importing modules"
import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z=mc.player.getPos()

for i in range(255):
	mc.setBlock(x+i,y,z,i)