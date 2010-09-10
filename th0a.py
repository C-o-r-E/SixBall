##############################
#####import stuff
##############################
import sys
import pygame
from pygame.locals import *

#############################
#initialize pygame
#############################
pygame.init()
pygame.display.set_caption("6 ball")
screen = pygame.display.set_mode((640, 360))
pygame.key.set_repeat(5, 50)
sakuya = pygame.time.Clock()

############################
#load things
############################

#the files
img_fullBG = "bgbig.png"
img_planet = "circle.png"
img_meow = "rin.png"
img_unyuu = "Raven.png"

#now we actually load the graphics in to memory (but only
#once)
orig_planet = pygame.image.load(img_planet).convert_alpha()
orig_bigBG = pygame.image.load(img_fullBG).convert_alpha()
orig_meow = pygame.image.load(img_meow).convert_alpha()
orig_unyuu = pygame.image.load(img_unyuu).convert_alpha()

#these are the surfaces that will appear on the screen and
#will be generated from the originals 
planet = orig_planet.copy()
meow = orig_meow.copy()


fpsFont = pygame.font.Font(None, 17)


#game loop

##handle input
##update sprites
##render
