# Houses bigger, fixed locations, titles for stations, exit house
# tracking: time spent off target, use different joysticks, switch fruits
# original collecting game: collecting in certain time
# pattern game: arrows move down, check collision and joystick pos, 3 fingers, increase speed after certain score

import pygame
import sys
import os
import subprocess
import random

f = open("highscores.txt", "r")
highscores = []

for line in f:
    line = line.split()
    highscores.append(int(line[-1]))

# Initialize Pygame
pygame.init()

# Set window dimensions
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Set colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Create window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set caption
pygame.display.set_caption("Dexterity-Dash")

# Set clock
clock = pygame.time.Clock()

# Set box dimensions
BOX_WIDTH = 50
BOX_HEIGHT = 50

box_img = pygame.image.load('player.png')
box_img = pygame.transform.scale(box_img, (BOX_WIDTH, BOX_HEIGHT))
inverted_box_img = pygame.transform.flip(box_img, True, False)

# Set box position
box_x = WINDOW_WIDTH // 2
box_y = WINDOW_HEIGHT // 2

# Set box speed
box_speed = 1

# Set direction constants
LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'

# Set initial direction
direction = RIGHT

# Load station images
station1_img = pygame.image.load('house1.png')
station2_img = pygame.image.load('house2.png')
station3_img = pygame.image.load('house3.png')

# Scale the station images to the desired size
station1_img = pygame.transform.scale(station1_img, (75, 75))
station2_img = pygame.transform.scale(station2_img, (75, 75))
station3_img = pygame.transform.scale(station3_img, (75, 75))

# Define station rectangles to be spawned at random locations
station1_rect = station1_img.get_rect()
station1_rect.x = random.randint(0, WINDOW_WIDTH - station1_rect.width)
station1_rect.y = random.randint(0, WINDOW_HEIGHT - station1_rect.height)

station2_rect = station2_img.get_rect()
station2_rect.x = random.randint(0, WINDOW_WIDTH - station2_rect.width)
station2_rect.y = random.randint(0, WINDOW_HEIGHT - station2_rect.height)

station3_rect = station3_img.get_rect()
station3_rect.x = random.randint(0, WINDOW_WIDTH - station3_rect.width)
station3_rect.y = random.randint(0, WINDOW_HEIGHT - station3_rect.height)

# Define station actions
station1_action = "station1.py"
station2_action = "station2.py"
station3_action = "station3.py"

# Load splash screen image
splash_screen = pygame.image.load('splash_screen.jpg')

# Scale the splash screen image to fit the window size
splash_screen = pygame.transform.scale(splash_screen, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Initialize Pygame's mixer module
pygame.mixer.init()

# Load the music file
pygame.mixer.music.load("background_music.mp3")

# Start playing the music on a loop
pygame.mixer.music.play(-1)

# Display splash screen
screen.blit(splash_screen, (0, 0))
pygame.display.flip()

# Wait for 2 seconds
pygame.time.wait(4000)

# Load background image
background = pygame.image.load('background.png')

# Scale the background image to fit the window size
background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Display background image
screen.blit(background, (0, 0))
pygame.display.flip()

box_vel_x = 0
box_vel_y = 0

# Create a font object
header_font = pygame.font.Font("font.otf", 48)
text_font = pygame.font.Font("font.otf", 36)

# Render the text onto a surface
text_header = header_font.render(f"Highscores:", True, blue)
text_st1 = text_font.render(f"Station 1: {highscores[0]}", True, blue)
text_st2 = text_font.render(f"Station 2: {highscores[1]}", True, blue)
text_st3 = text_font.render(f"Station 3: {highscores[2]}", True, blue)

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()

    # Handle user input and update velocity
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        box_vel_x -= box_speed
        direction = LEFT
    if keys[pygame.K_RIGHT]:
        box_vel_x += box_speed
        direction = RIGHT
    if keys[pygame.K_UP]:
        box_vel_y -= box_speed
        direction = UP
    if keys[pygame.K_DOWN]:
        box_vel_y += box_speed
        direction = DOWN

    box_vel_x *= 0.9
    box_vel_y *= 0.9

    # Update box position
    box_x += box_vel_x
    box_y += box_vel_y

    if box_x < 0:
        box_x = 0
    elif box_x > WINDOW_WIDTH - BOX_WIDTH:
        box_x = WINDOW_WIDTH - BOX_WIDTH
    if box_y < 0:
        box_y = 0
    elif box_y > WINDOW_HEIGHT - BOX_HEIGHT:
        box_y = WINDOW_HEIGHT - BOX_HEIGHT

    # Check if box is overlapping with any station
    if station1_rect.colliderect(pygame.Rect(box_x, box_y, BOX_WIDTH, BOX_HEIGHT)):
        # Show prompt for station 1
        pygame.mixer.music.pause()
        print("You have reached station 1!")
        subprocess.call(["python", station1_action])
        pygame.mixer.music.unpause()
        box_x = WINDOW_WIDTH // 2
        box_y = WINDOW_HEIGHT // 2
    elif station2_rect.colliderect(pygame.Rect(box_x, box_y, BOX_WIDTH, BOX_HEIGHT)):
        # Show prompt for station 2
        pygame.mixer.music.pause()
        print("You have reached station 2!")
        subprocess.call(["python", station2_action])
        pygame.mixer.music.unpause()
        box_x = WINDOW_WIDTH // 2
        box_y = WINDOW_HEIGHT // 2
    elif station3_rect.colliderect(pygame.Rect(box_x, box_y, BOX_WIDTH, BOX_HEIGHT)):
        # Show prompt for station 3
        pygame.mixer.music.pause()
        print("You have reached station 3!")
        subprocess.call(["python", station3_action])
        pygame.mixer.music.unpause()
        box_x = WINDOW_WIDTH // 2
        box_y = WINDOW_HEIGHT // 2
    # Draw objects
    screen.blit(background, (0, 0))
    screen.blit(station1_img, (station1_rect.x, station1_rect.y))
    screen.blit(station2_img, (station2_rect.x, station2_rect.y))
    screen.blit(station3_img, (station3_rect.x, station3_rect.y))
    if direction == LEFT:
        screen.blit(inverted_box_img, (box_x, box_y))
    else:
        screen.blit(box_img, (box_x, box_y))
    screen.blit(text_header, (WINDOW_WIDTH-text_header.get_width(), 0))
    screen.blit(text_st1, (WINDOW_WIDTH-text_st1.get_width(), text_header.get_height()))
    screen.blit(text_st2, (WINDOW_WIDTH-text_st2.get_width(), text_st1.get_height()+text_header.get_height()))
    screen.blit(text_st3, (WINDOW_WIDTH-text_st3.get_width(), text_st2.get_height()+text_st1.get_height()+text_header.get_height()))
    
    # Update display and tick clock
    pygame.display.update()
    clock.tick(60)