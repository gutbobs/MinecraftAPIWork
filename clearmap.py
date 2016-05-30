#!/usr/bin/env python
import sys
import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()
# wipe everything from map
mc.setBlocks(-128,0,-128,128,64,128,0)

# get block id
if (len(sys.argv) > 1):
	blockID = int(sys.argv[1])
else:
	blockID = 2


mc.setBlocks(-128,0,-128,128,-64,128,blockID)
