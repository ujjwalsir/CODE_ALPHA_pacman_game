pip install pygame

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PACMAN_RADIUS = 20
PACMAN_COLOR = (255, 255, 0)
BACKGROUND_COLOR = (0, 0, 0)

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pacman Game")

# Initialize Pacman's position
pacman_x = SCREEN_WIDTH // 2
pacman_y = SCREEN_HEIGHT // 2

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_x -= 5
    if keys[pygame.K_RIGHT]:
        pacman_x += 5
    if keys[pygame.K_UP]:
        pacman_y -= 5
    if keys[pygame.K_DOWN]:
        pacman_y += 5

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw Pacman
    pygame.draw.circle(screen, PACMAN_COLOR, (pacman_x, pacman_y), PACMAN_RADIUS)

    # Update the display
    pygame.display.update()
