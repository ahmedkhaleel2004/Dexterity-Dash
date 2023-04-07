import pygame
import random
import sys

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up the game
pygame.init()

# Set the screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the caption of the window
pygame.display.set_caption("Gardening Tracking Game")

# Set up the clock
clock = pygame.time.Clock()

# Set up the font
font = pygame.font.Font(None, 36)

# Define the class for the target
class Target(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += random.randint(-5, 5)
        self.rect.y += random.randint(-5, 5)

        # Keep the target on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# Create the target sprite
target_sprite = pygame.sprite.Group()
target = Target()
target_sprite.add(target)

# Set the initial score
score = 0

# Set up the game loop
done = False
while not done:
    # --- Event Processing ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic ---
    # Get the state of the arrow keys
    keys = pygame.key.get_pressed()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
    # Move the target based on the arrow keys
    if keys[pygame.K_LEFT]:
        target.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        target.rect.x += 5
    if keys[pygame.K_UP]:
        target.rect.y -= 5
    if keys[pygame.K_DOWN]:
        target.rect.y += 5

    # Check for collisions between the target and the mouse cursor
    mouse_pos = pygame.mouse.get_pos()
    if target.rect.collidepoint(mouse_pos):
        # Move the target to a new random location
        target.rect.x = random.randint(0, SCREEN_WIDTH - target.rect.width)
        target.rect.y = random.randint(0, SCREEN_HEIGHT - target.rect.height)

        # Increase the score
        score += 1

    # Update the target sprite
    target_sprite.update()

    # --- Draw the screen ---
    # Fill the background
    screen.fill(WHITE)

    # Draw the target sprite
    target_sprite.draw(screen)

    # Draw the score
    score_text = font.render("Score: {}".format(score), True, BLACK)
    screen.blit(score_text, [10, 10])

    # Update the screen
    pygame.display.flip()

    # --- Limit to 60 frames per second ---
    clock.tick(60)

# Close the window and quit.
pygame.quit()
