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
sprites_sheet = Spritesheet('./graphics/sprite.png')
dino = sprites_sheet.get_sprite(1338, 2, 88, 94)
ground = sprites_sheet.get_sprite(2, 104, 2400, 24)
score = game_font.render('00000', False, (83, 83, 83))


while True:
    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Draw objects
    screen.blit(dino,(0, HEIGHT - 98))
    screen.blit(ground, (0, HEIGHT - 28))
    screen.blit(score, (WIDTH - 100, 10))
    # Update display
    pygame.display.update()
    clock.tick(60)