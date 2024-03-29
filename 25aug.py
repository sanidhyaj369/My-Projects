import pygame
import random

pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake and Ladder Game")

white = (255, 255, 255)

player_image = pygame.image.load("blue.png")
player_image=pygame.transform.scale(player_image,(32,32))
# Load snake and ladder images if needed

player_x, player_y = 0, height - 50

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5

    screen.fill(white)
    screen.blit(player_image, (player_x, player_y))

    pygame.display.flip()

pygame.quit()
