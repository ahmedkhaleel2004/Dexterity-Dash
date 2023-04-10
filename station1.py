import pygame
import random
import sys
import time
from joystick_library import Joystick

joystick1 = Joystick("4B",1,0)
joystick2 = Joystick("4B",2,3)
joystick3 = Joystick("48",3,2)
joystick4 = Joystick("49",1,0)
joystick5 = Joystick("49",2,3)

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

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
font_number = pygame.font.Font("font.otf", 150)

background = pygame.image.load('background.png')

# Scale the background image to fit the window size
background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))

# # Initialize Pygame's mixer module
# pygame.mixer.init()

# # Load the music file
# pygame.mixer.music.load("station1.mp3")

# # Start playing the music on a loop
# pygame.mixer.music.play(-1)

screen.blit(background, (0, 0))

joysticks = [joystick1, joystick2, joystick3, joystick4, joystick5]

start_text = font.render("Game Starting in...", True, BLUE)
three_text = font_number.render("3", True, BLUE)
two_text = font_number.render("2", True, BLUE)
one_text = font_number.render("1", True, BLUE)
screen.blit(start_text, (WINDOW_WIDTH // 2 - start_text.get_width() // 2, WINDOW_HEIGHT // 2 - start_text.get_height() // 2 - 200))
screen.blit(three_text, (WINDOW_WIDTH // 2 - three_text.get_width() // 2, WINDOW_HEIGHT // 2 - three_text.get_height() // 2))
pygame.display.flip()
time.sleep(1)
screen.blit(background, (0, 0))
screen.blit(start_text, (WINDOW_WIDTH // 2 - start_text.get_width() // 2, WINDOW_HEIGHT // 2 - start_text.get_height() // 2 - 200))
screen.blit(two_text, (WINDOW_WIDTH // 2 - two_text.get_width() // 2, WINDOW_HEIGHT // 2 - two_text.get_height() // 2))
pygame.display.flip()
time.sleep(1)
screen.blit(background, (0, 0))
screen.blit(start_text, (WINDOW_WIDTH // 2 - start_text.get_width() // 2, WINDOW_HEIGHT // 2 - start_text.get_height() // 2 - 200))
screen.blit(one_text, (WINDOW_WIDTH // 2 - one_text.get_width() // 2, WINDOW_HEIGHT // 2 - one_text.get_height() // 2))
pygame.display.flip()
time.sleep(1)
screen.blit(background, (0, 0))

def draw_circles():
    # Define the radius of the circles
    CIRCLE_RADIUS = 50

    # Define the space between the circles
    CIRCLE_SPACING = 10

    # Calculate the x-coordinate of the leftmost circle
    circles_start_x = WINDOW_WIDTH // 2 - CIRCLE_RADIUS * 4 - CIRCLE_SPACING * 3

    # Define the y-coordinate of the circles
    CIRCLE_Y = 300

    # Draw the circles
    for i in range(5):
        circle_x = circles_start_x + i * (CIRCLE_RADIUS * 2 + CIRCLE_SPACING*2)
        pygame.draw.circle(screen, BLACK, (circle_x, CIRCLE_Y), CIRCLE_RADIUS, 5)

def drop_directions():
    global selected_circle
    global selected_direction

    # Define the directions images
    directions_images = ["arrowup.png", "arrowdown.png", "arrowleft.png", "arrowright.png"]

    # Randomly select 3 directions
    selected_direction = random.sample(directions_images, 1)

    # Define the y-coordinate of the directions
    DIRECTION_Y = 0

    # Define the speed of the directions
    DIRECTION_SPEED = 2

    # Define the radius of the circles
    CIRCLE_RADIUS = 50

    # Define the space between the circles
    CIRCLE_SPACING = 10

    # Calculate the x-coordinate of the leftmost circle
    circles_start_x = WINDOW_WIDTH // 2 - CIRCLE_RADIUS * 4 - CIRCLE_SPACING * 3
    # Define the y-coordinate of the circles

    # Randomly select 3 circles
    selected_circle = random.sample(range(5), 1)

    # Load the directions images
    directions = []
    for direction in selected_direction:
        directions.append(pygame.image.load(direction))

    # Scale the directions images to fit the circle size
    for i in range(len(directions)):
        directions[i] = pygame.transform.scale(directions[i], (75, 75))

    CIRCLE_Y = 300 - directions[0].get_height() // 2

    # Set the x-coordinate of the directions to the center of the selected circles
    direction_x = []
    for circle_index in selected_circle:
        circle_x = circles_start_x + circle_index * (CIRCLE_RADIUS * 2 + CIRCLE_SPACING*2)
        direction_x.append(circle_x - directions[0].get_width() // 2)

    # Start dropping the directions
    while DIRECTION_Y <= CIRCLE_Y:
        # --- Event Processing ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # --- Game logic ---
        # Move the directions down
        DIRECTION_Y += DIRECTION_SPEED

        # Draw the circles
        screen.blit(background, (0, 0))
        draw_circles()

        # Draw the directions
        for i in range(len(directions)):
            screen.blit(directions[i], (direction_x[i], DIRECTION_Y))

        # Update the screen
        pygame.display.flip()

        # --- Limit to 60 frames per second ---
        clock.tick(60)

def check():
    global score
    for i in range(5):
        if i == num:
            if selected_direction == ["arrowup.png"]:
                if joysticks[i].read_y() > 0.1:
                    score += 1
            elif selected_direction == ["arrowdown.png"]:
                if joysticks[i].read_y() < -0.1:
                    score += 1
            elif selected_direction == ["arrowleft.png"]:
                if joysticks[i].read_x() < -0.1:
                    score += 1
            elif selected_direction == ["arrowright.png"]:
                if joysticks[i].read_x() > 0.1:
                    score += 1

draw_circles()

score = 0

# Set up the game loop
running = True
while running:
    # --- Event Processing ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    drop_directions()
    
    # check if selected circle joystick is in the right direction
    num = selected_circle[0]

    for i in range(20):
        check()
        time.sleep(0.001)

    # Update the screen
    pygame.display.flip()

    # --- Limit to 60 frames per second ---
    clock.tick(60)

# Close the window and quit.
pygame.quit()