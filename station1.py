import pygame
import random
import sys
from joystick_library import Joystick

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Set the width and height of the screen [width, height]
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Set up the game
pygame.init()

# Set the screen
screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

# Set the caption of the window
pygame.display.set_caption("Pattern Matching")

# Set up the clock
clock = pygame.time.Clock()

# Set up the font
font = pygame.font.Font("font.otf", 36)

background = pygame.image.load('background.png')

# Scale the background image to fit the window size
background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Initialize Pygame's mixer module
pygame.mixer.init()

# Load the music file
pygame.mixer.music.load("station1.mp3")

# Start playing the music on a loop
pygame.mixer.music.play(-1)

# Set up the game loop
running = True
while running:
    # --- Event Processing ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Game logic ---
    # Get the state of the arrow keys
    keys = pygame.key.get_pressed()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

    # Move the target based on the arrow keys
    screen.blit(background, (0, 0))

    # Update the screen
    pygame.display.flip()

    # --- Limit to 60 frames per second ---
    clock.tick(60)

# Close the window and quit.
pygame.quit()

'''
    if keys[pygame.K_LEFT]:
        
    if keys[pygame.K_RIGHT]:
        
    if keys[pygame.K_UP]:
        
    if keys[pygame.K_DOWN]:
'''