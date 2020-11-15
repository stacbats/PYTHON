import pygame
import random
import sys
from gameLoop import *

import settings

pygame.init()
w_width = 800
w_height = 600
gameDisplay = pygame.display.set_mode((w_width, w_height))      # this is creating the display
eye_image = pygame.image.load('eye.png')                      # load the image

pygame.display.set_caption('Eye in a Box')

gameplay(gameDisplay, eye_image)

pygame.quit()
sys.exit


