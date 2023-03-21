import pygame
import random

# Initialize Pygame
pygame.init()
score =0
# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dot Tracking Game")

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set up the dot
dot_size = 20
dot_x = screen_width / 2 - dot_size / 2
dot_y = screen_height / 2 - dot_size / 2
dot_speed = 5
dot_color = white

# Set up the target
target_size = 40
target_x = random.randint(0, screen_width - target_size)
target_y = random.randint(0, screen_height - target_size)
target_speed = 2
target_color = red

# Set up the clock
clock = pygame.time.Clock()

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        dot_y -= dot_speed
    if keys[pygame.K_s]:
        dot_y += dot_speed
    if keys[pygame.K_a]:
        dot_x -= dot_speed
    if keys[pygame.K_d]:
        dot_x += dot_speed

    # Update the dot
    dot_rect = pygame.Rect(dot_x, dot_y, dot_size, dot_size)

    # Update the target
    target_x += random.randint(-target_speed, target_speed)
    target_y += random.randint(-target_speed, target_speed)
    target_rect = pygame.Rect(target_x, target_y, target_size, target_size)

    # Draw the dot and the target
    screen.fill(black)
    pygame.draw.rect(screen, dot_color, dot_rect)
    pygame.draw.rect(screen, target_color, target_rect)

    # Check for collision between the dot and the target
    if dot_rect.colliderect(target_rect):
        target_x = random.randint(0, screen_width - target_size)
        target_y = random.randint(0, screen_height - target_size)
        score +=1
    # Update the screen
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
print("Your final score was",score)
