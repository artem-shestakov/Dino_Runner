import imp
import pygame
from spritesheet import Spritesheet
from sys import exit

WIDTH = 800
HEIGHT = 400
FONT_SIZE = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((247,247,247))
clock = pygame.time.Clock()
pygame.display.set_caption("Runner game")

# Font
game_font = pygame.font.Font('fonts/arcade_classic.ttf', FONT_SIZE)

# Sprites
backgrounds = Spritesheet('./graphics/backgrounds.png')
background = backgrounds.get_sprite(0, 0, 231, 63)
background = pygame.transform.scale(background, (800, 300))

sprite_sheets = Spritesheet('./graphics/spritesheet.png')
ground = sprite_sheets.get_sprite(72, 96, 20, 20)
ground = pygame.transform.scale(ground, (100, 100))

player = pygame.image.load('graphics/player/alienGreen_stand.png')

while True:
    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Draw objects
    screen.blit(background, (0,0))
    for x in range(0,800,100):
        screen.blit(ground, (x, 300))
    screen.blit(player, (50, 300-92))

    # Update display
    pygame.display.update()
    clock.tick(60)