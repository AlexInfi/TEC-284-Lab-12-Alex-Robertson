# Import the API
from mcpi_addons.minecraft import Minecraft

#Initialize the API (MCPI must be open and in a world at this time)
mc = Minecraft.create()
import time

#while loop to create the block trail
count = 0
while count < 30:
    pos = mc.player.getPos()
    mc.setBlock(pos.x, pos.y - 1, pos.z, 12)
    time.sleep(1)
    count += 1

