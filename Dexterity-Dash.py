import pygame
import random


from sensor_library import *
import time

joystick1 = Force_Sensing_Resistor(0)
joystick2 = Force_Sensing_Resistor(1)
UD = []
LR = []
SIZE = 10 # Window of rolling average

# Baseline is the idling value maually found for X and Y respectively
BASELINE_X = 132
BASELINE_Y = 124

def rolling_average(size, data):
    data = data[len(data)-size:len(data)]
    average = sum(data)/size
    return average

def scale(value, baseline):
    scaled_value = ((value-baseline)/baseline)*2
    return scaled_value



# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dexterity Dash")

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set up the dot
dot_size = 20
dot_x = screen_width // 2 - dot_size // 2
dot_y = screen_height // 2 - dot_size // 2
dot_speed = 2
dot_color = white
dot_vel_x = 0
dot_vel_y = 0

# Set up the target
target_size = 40
target_x = random.randint(0, screen_width - target_size)
target_y = random.randint(0, screen_height - target_size)
target_color = red

# Set up the clock
clock = pygame.time.Clock()

# Set up the title screen loop
title_active = True
while title_active:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                title_active = False
                quit()
    
        # Handle user input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            title_active = False
    
        # Draw the title
        screen.fill(black)
        bigfont = pygame.font.SysFont("impact", 100)
        smallfont = pygame.font.SysFont("impact", 50)
        text1 = bigfont.render("Dexterity Dash", 1, white)
        text2 = smallfont.render("Press Space to Start", 1, red)
        screen.blit(text1, (screen_width // 2 - text1.get_width() // 2, screen_height // 2 - text1.get_height() // 2 - 100))
        screen.blit(text2, (screen_width // 2 - text2.get_width() // 2, screen_height // 2 - text2.get_height() // 2 + 100))
    
        # Update the screen
        pygame.display.update()
    
        # Set the frame rate
        clock.tick(60)

# Set up the game loop
score = 0
game_active = True
while game_active:

    # Append raw data
    UD.append(joystick1.force_raw())
    LR.append(joystick2.force_raw())

    # Clear lists
    if len(UD) > SIZE*2:
        UD.pop(0)
    if len(LR) > SIZE*2:
        LR.pop(0)

    # Calculate movement
    average_x = rolling_average(SIZE,LR)
    scaled_x = scale(average_x,BASELINE_X)
    average_y = rolling_average(SIZE,UD)
    scaled_y = scale(average_y, BASELINE_Y)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False

    # Move dot
    dot_vel_y += (scaled_y*-1)*4
    dot_vel_x += (scaled_x)*4

    # Add friction
    dot_vel_x *= 0.7
    dot_vel_y *= 0.7

    # Update the crosshair position
    dot_x += dot_vel_x
    dot_y += dot_vel_y

    # Set boundaries for the dot
    if dot_x <= 0:
        dot_x = 0
    if dot_x >= screen_width - dot_size:
        dot_x = screen_width - dot_size
    if dot_y <= 0:
        dot_y = 0
    if dot_y >= screen_height - dot_size:
        dot_y = screen_height - dot_size

    # Update the dot
    dot_rect = pygame.Rect(dot_x, dot_y, dot_size, dot_size)

    # Update the target
    target_rect = pygame.Rect(target_x, target_y, target_size, target_size)

    # Check for collision between the dot and the target
    if dot_rect.colliderect(target_rect):
        target_x = random.randint(0, screen_width - target_size)
        target_y = random.randint(0, screen_height - target_size)
        score += 1

    # Draw the dot and the target
    screen.fill(black)
    pygame.draw.rect(screen, dot_color, dot_rect)
    pygame.draw.rect(screen, target_color, target_rect)

    # Update the screen
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
print("Your final score was", score)
