import pygame
import random

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
time_left = 3000
fruits = ["apple", "tree", "rose"]
fruit_images = {
    "apple": pygame.image.load("apple.png"),
    "tree": pygame.image.load("tree.png"),
    "rose": pygame.image.load("rose.png")
}
fruit_rects = {
    "apple": fruit_images["apple"].get_rect(),
    "tree": fruit_images["tree"].get_rect(),
    "rose": fruit_images["rose"].get_rect()
}
fruit_positions = {
    "apple": [SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2],
    "tree": [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2],
    "rose": [SCREEN_WIDTH // 4 * 3, SCREEN_HEIGHT // 2]
}
fruit_velocities = {
    "apple": [random.uniform(-3, 3), random.uniform(-3, 3)],
    "tree": [random.uniform(-3, 3), random.uniform(-3, 3)],
    "rose": [random.uniform(-3, 3), random.uniform(-3, 3)]
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

# Start the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw the fruits
    for fruit in fruits:
        draw_fruit(fruit)

    # Draw the score
    draw_text(f"Score: {score}", BLACK, SCREEN_WIDTH // 2, 50)

    # Draw the time left
    draw_text(f"Time Left: {time_left // 1000}", BLACK, SCREEN_WIDTH // 2, 100)
    
    #update fruit positions
    update_fruit_positions()

    # Move the black square with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        shovel_rect.move_ip(-5, 0)
    if keys[pygame.K_RIGHT]:
        shovel_rect.move_ip(5, 0)
    if keys[pygame.K_UP]:
        shovel_rect.move_ip(0, -5)
    if keys[pygame.K_DOWN]:
        shovel_rect.move_ip(0, 5)

    # Check for collisions with the black square
    for fruit in fruits:
        if fruit_rects[fruit].colliderect(shovel_rect):
            score += 1
            fruits.remove(fruit)
            fruits.append(random_fruit())
            print("Collision detecterd, random fruit spawned")

    # Check if time is up
    if time_left <= 0:
        running = False

    # Draw the black square
    pygame.draw.rect(screen, BLACK, shovel_rect)

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
pygame.display.update()

# Wait for a while before quitting
pygame.time.wait(2000)

# Quit pygame
pygame.quit()
