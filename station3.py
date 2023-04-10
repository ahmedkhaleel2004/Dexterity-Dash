import pygame
import random
import time
from joystick_library import *
from update_func import update_score

joystick1 = Joystick("4B",1,0)
joystick2 = Joystick("4B",2,3)
joystick3 = Joystick("48",3,2)
joystick4 = Joystick("49",1,0)
joystick5 = Joystick("49",2,3)
pygame.init()

# Define the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Define the font
FONT = pygame.font.SysFont(None, 36)



# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the caption
pygame.display.set_caption("Harvest Time")

# Define the game clock
clock = pygame.time.Clock()

# Define the game variables
score = 0
time_left = 4000
background_image = pygame.image.load("Selection.PNG").convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
fruits = ["apple", "tree"]
fruit_images = {
    "apple": pygame.image.load("orange.PNG"),
    "tree": pygame.image.load("tree.PNG")
}
for i in fruit_images:
    fruit_images[i] = pygame.transform.scale(fruit_images[i], (50, 50))
fruit_rects = {
    "apple": fruit_images["apple"].get_rect(),
    "tree": fruit_images["tree"].get_rect()
}
fruit_positions = {
    "apple": [SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2],
    "tree": [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
}
speed=1.5
fruit_velocities = {
    "apple": [random.uniform(-speed, speed), random.uniform(-speed, speed)],
    "tree": [random.uniform(-speed, speed), random.uniform(-speed, speed)]
}

# Define the functions
def draw_text(text, color, x, y):
    surface = FONT.render(text, True, color)
    rect = surface.get_rect()
    rect.center = (x, y)
    screen.blit(surface, rect)

def draw_fruit(fruit):
    screen.blit(fruit_images[fruit], fruit_rects[fruit])

def update_fruit_positions():
    for fruit in fruits:
        # Update the position based on the velocity
        fruit_positions[fruit][0] += fruit_velocities[fruit][0]
        fruit_positions[fruit][1] += fruit_velocities[fruit][1]

        # Bounce off the edges of the screen
        if fruit_positions[fruit][0] < 0 or fruit_positions[fruit][0] > SCREEN_WIDTH:
            fruit_velocities[fruit][0] *= -1
        if fruit_positions[fruit][1] < 0 or fruit_positions[fruit][1] > SCREEN_HEIGHT:
            fruit_velocities[fruit][1] *= -1

        # Update the fruit_rect with the new position
        fruit_rects[fruit].center = fruit_positions[fruit]

def random_fruit():
    return random.choice(fruits)

# Create the black square
shovel_rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 20, 20)

# Set up the dot
dot_size = 20
dot_x = SCREEN_WIDTH // 2 - dot_size // 2
dot_y = SCREEN_HEIGHT // 2 - dot_size // 2
dot_speed = 2
dot_color = WHITE
dot_vel_x = 0
dot_vel_y = 0
a=1
joysticks = [joystick1,joystick2,joystick3,joystick4,joystick5]
score = 0
# Start the game loop
running = True

start = time.time()

while running:

    current = time.time()
    elapsed = current - start
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    #Draw the background
    screen.blit(background_image, [0, 0])


    # Draw the fruits
    for fruit in fruits:
        draw_fruit(fruit)

    # Draw the score
    draw_text(f"Score: {score}", BLACK, SCREEN_WIDTH // 2, 50)

    # Draw the time left
    draw_text(f"Time Left: {30 - elapsed: 0.2f}", BLACK, SCREEN_WIDTH // 2, 100)
    
    #update fruit positions
    update_fruit_positions()

    # Handle user input and update velocity
    if a ==1 or a==3 or a==4:
        y_inputs = joysticks[a-1].read_x()
        x_inputs = joysticks[a-1].read_y()

        dot_vel_y += x_inputs*-25
        dot_vel_x += y_inputs*25
    elif a ==5:
        y_inputs = joysticks[a-1].read_x()
        x_inputs = joysticks[a-1].read_y()

        dot_vel_y += y_inputs*25
        dot_vel_x += x_inputs*-25
        

    else:
        a = 1

    draw_text(f"Current joystick: {a}", BLACK, 120, 30)
        
   # Add friction
    dot_vel_x *= 0.1
    dot_vel_y *= 0.1

    # Update the crosshair position
    dot_x += dot_vel_x
    dot_y += dot_vel_y

    # Check for collisions with the black square
    for fruit in fruits:
        if fruit_rects[fruit].colliderect(pygame.Rect(dot_x, dot_y, dot_size, dot_size)):

            score += 1
            fruits.remove(fruit)
            fruits.append(random_fruit())
            a=random.randint(1,5)
    # Check if time is up
    if elapsed > 30:
        running = False

    # Draw the black square
    pygame.draw.rect(screen, dot_color, (dot_x, dot_y, dot_size, dot_size))

    # Update the screen
    pygame.display.update()

    # Decrement the time

    time_left -= 1

    # Tick the clock
    clock.tick(60)

# Game over
screen.fill(WHITE)  
draw_text("Game Over", BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
draw_text(f"Final Score: {score}", BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

update_score(3, score)

def update_highscores():
    f = open("highscores.txt", "r")
    highscores = []

    for line in f:
        line = line.split()
        highscores.append(int(line[-1]))

    f.close()
    return highscores

high_score = update_highscores()[-1]

highscores = update_highscores()

if high_score > score:
    draw_text(f"The current high score is {high_score}", BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
else:
    draw_text(f"The current high score is {score}", BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)


pygame.display.update()

# Wait for a while before quitting
pygame.time.wait(3000)

# Quit pygame
pygame.quit()
