import pygame
import sys
import os
import subprocess





# Initialize Pygame
pygame.init()

# Set window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Set colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Create window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set caption
pygame.display.set_caption("Square Box Character")

# Set clock
clock = pygame.time.Clock()

# Set box dimensions
BOX_WIDTH = 16
BOX_HEIGHT = 16

# Set box position
box_x = WINDOW_WIDTH // 2
box_y = WINDOW_HEIGHT // 2

# Set box speed
box_speed = 5

# Set direction constants
LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'

# Set initial direction
direction = RIGHT

# Define station rectangles
station1_rect = pygame.Rect(200, 200, 50, 50)
station2_rect = pygame.Rect(500, 400, 50, 50)
station3_rect = pygame.Rect(100, 500, 50, 50)

# Define station actions
station1_action = "station1.py"
station2_action = "station2.py"
station3_action = "station3.py"

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Handle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        box_x -= box_speed
        direction = LEFT
    if keys[pygame.K_RIGHT]:
        box_x += box_speed
        direction = RIGHT
    if keys[pygame.K_UP]:
        box_y -= box_speed
        direction = UP
    if keys[pygame.K_DOWN]:
        box_y += box_speed
        direction = DOWN
    
    # Check if box is overlapping with any station
    if station1_rect.colliderect(pygame.Rect(box_x, box_y, BOX_WIDTH, BOX_HEIGHT)):
        # Show prompt for station 1
        print("You have reached station 1!")
        subprocess.call(["python", station1_action])
        box_x+=50
        box_y+=50
    elif station2_rect.colliderect(pygame.Rect(box_x, box_y, BOX_WIDTH, BOX_HEIGHT)):
        # Show prompt for station 2
        print("You have reached station 2!")
        subprocess.call(["python", station2_action])
        box_x+=50
        box_y+=50
    elif station3_rect.colliderect(pygame.Rect(box_x, box_y, BOX_WIDTH, BOX_HEIGHT)):
        # Show prompt for station 3
        print("You have reached station 3!")
        subprocess.call(["python", station3_action])
        box_x+=50
        box_y+=50
    # Draw objects
    screen.fill(black)
    pygame.draw.rect(screen, red, station1_rect)
    pygame.draw.rect(screen, blue, station2_rect)
    pygame.draw.rect(screen, green, station3_rect)
    
    if direction == LEFT:
        pygame.draw.rect(screen, white, (box_x, box_y, BOX_WIDTH, BOX_HEIGHT))
    elif direction == RIGHT:
        pygame.draw.rect(screen, white, (box_x, box_y, BOX_WIDTH, BOX_HEIGHT))
    elif direction == UP:
        pygame.draw.rect(screen, white, (box_x, box_y, BOX_WIDTH, BOX_HEIGHT))
    elif direction == DOWN:
        pygame.draw.rect(screen, white, (box_x, box_y, BOX_WIDTH, BOX_HEIGHT))
    
    # Update display and tick clock
    pygame.display.update()
    clock.tick(60)
