# MinecraftAPIWork
repository of files used for working with the Minecraft API on a raspberry pi

Description of files:

Blockref.py = creates all block types and then outputs them. Refer to this page (http://www.raspberrypi-spy.co.uk/2014/09/raspberry-pi-minecraft-block-id-number-reference/) for a reference/

clearmap.py = clears the whole map and puts a flat grass floor in it. You can also provide an argument to choose your own block type. Refer to the block id reference page mentioned above

photoToMinecraft.py = converts a photo to a grey scale minecraft image. Limited in size to ~100pixels due to short drawing distance on the raspberry pi

zoomBlock.py = makes a block zoom into position. Blocks can zoom in the x,y,z dimensions. zooming blocks will delete any existing blocks that they come into contact with.