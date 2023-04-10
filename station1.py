import pygame
import random
import sys
import time

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

# Initialize Pygame's mixer module
pygame.mixer.init()

# Load the music file
pygame.mixer.music.load("station1.mp3")

# Start playing the music on a loop
pygame.mixer.music.play(-1)

screen.blit(background, (0, 0))

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
    # Define the directions images
    directions_images = ["arrowup.png", "arrowdown.png", "arrowleft.png", "arrowright.png"]

    # Randomly select 3 directions
    selected_directions = random.sample(directions_images, 3)

    # Define the y-coordinate of the directions
    DIRECTION_Y = 0

    # Define the speed of the directions
    DIRECTION_SPEED = 5

    # Define the radius of the circles
    CIRCLE_RADIUS = 50

    # Define the space between the circles
    CIRCLE_SPACING = 10

    # Calculate the x-coordinate of the leftmost circle
    circles_start_x = WINDOW_WIDTH // 2 - CIRCLE_RADIUS * 4 - CIRCLE_SPACING * 3
    # Define the y-coordinate of the circles
    CIRCLE_Y = 300

    # Randomly select 3 circles
    selected_circles = random.sample(range(5), 3)

    # Load the directions images
    directions = []
    for direction in selected_directions:
        directions.append(pygame.image.load(direction))

    # Scale the directions images to fit the circle size
    for i in range(len(directions)):
        directions[i] = pygame.transform.scale(directions[i], (75, 75))

    # Set the x-coordinate of the directions to the center of the selected circles
    direction_x = []
    for circle_index in selected_circles:
        circle_x = circles_start_x + circle_index * (CIRCLE_RADIUS * 2 + CIRCLE_SPACING*2)
        direction_x.append(circle_x + CIRCLE_RADIUS - directions[0].get_width() // 2)

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

draw_circles()
drop_directions()

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

    # Update the screen
    pygame.display.flip()

    # --- Limit to 60 frames per second ---
    clock.tick(60)

# Close the window and quit.
pygame.quit()