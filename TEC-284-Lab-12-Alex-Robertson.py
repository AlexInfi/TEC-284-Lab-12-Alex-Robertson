# Import the api
from mcpi_addons.minecraft import Minecraft
# Initialize the api (MCPI must be open and in a world at this time)
mc = Minecraft.create()

mc.postToChat("Hello World!")

# Coordinates variables
x = input ("X Coordinate: ")
y = input ("Y Coordinate: ")
z = input ("Z Coordinate: ")

# Casts the Coordinates as integers
x = int(x)
y = int(y)
z = int(z)

# House Dimension variables
width = input ("House Width: ")
length = input ("House Length: ")
height = input ("House Height: ")

width = int(width)
length = int(length)
height = int(height)

# Creates the house using the player's teleported position
mc.setBlocks(x, y, z, x + width, y + height, z + length, 3)

# Uses air blocks to make the house hollow
mc.setBlocks(x+1, y, z+1, x + (width - 1), y + (height - 1), z + (length - 1), 0)