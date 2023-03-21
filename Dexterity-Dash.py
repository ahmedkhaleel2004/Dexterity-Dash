import pygame
import random

# Initialize Pygame
pygame.init()
score =0
# Set up the screen
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dexterity Dash")

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# # Set up the fonts
# font = pygame.font.Font("GoudyStoutRegular.ttf", 60)

# # Set up the main menu
# menu_title = font.render("Dexterity Dash", True, white)
# menu_title_rect = menu_title.get_rect(center=(screen_width/2, 200))

# play_button = font.render("Play", True, white)
# play_button_rect = play_button.get_rect(center=(screen_width/2, 400))

# # Set up the game loop
game_active = True
# menu_active = True
# while menu_active:

#     # Handle events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             menu_active = False

#     # Handle user input
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_SPACE]:
#         game_active = True
#         menu_active = False

#     # Draw the menu screen
#     screen.fill(black)
#     text = font.render("Dexterity Dash", True, white)
#     text_rect = text.get_rect(center=(screen_width/2, screen_height/2))
#     screen.blit(text, text_rect)
#     pygame.display.update()

# Set up the dot
dot_size = 20
dot_x = screen_width / 2 - dot_size / 2
dot_y = screen_height / 2 - dot_size / 2
dot_speed = 2
dot_color = white

# Set up the target
target_size = 40
target_x = random.randint(0, screen_width - target_size)
target_y = random.randint(0, screen_height - target_size)
target_color = red

# Set up the clock
clock = pygame.time.Clock()

dot_vel_x = 0
dot_vel_y = 0

while game_active:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False

    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        dot_vel_y -= dot_speed
    if keys[pygame.K_s]:
        dot_vel_y += dot_speed
    if keys[pygame.K_a]:
        dot_vel_x -= dot_speed
    if keys[pygame.K_d]:
        dot_vel_x += dot_speed

    dot_vel_x *= 0.9
    dot_vel_y *= 0.9

    # Update the crosshair position
    dot_x += dot_vel_x
    dot_y += dot_vel_y

    # Update the dot
    dot_rect = pygame.Rect(dot_x, dot_y, dot_size, dot_size)

    # Update the target
    
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
