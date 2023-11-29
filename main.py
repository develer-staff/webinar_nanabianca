import argparse
import os

import pygame

import grid

parser = argparse.ArgumentParser(
    prog="Conway game of life", description="Pygame emulation of Conway game of life"
)
parser.add_argument(
    "-f", "--filename", required=False, help="path to grid file to load"
)
args = parser.parse_args()

os.environ["SDL_VIDEO_CENTERED"] = "1"

# resolution
width, height = 1920, 1080
size = (width, height)

pygame.init()
pygame.display.set_caption("CONWAY'S GAME OF LIFE")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 30

black = (0, 0, 0)
blue = (0, 121, 150)
blue1 = (0, 14, 71)
white = (255, 255, 255)

scaler = 30
offset = 1

Grid = grid.Grid(width, height, scaler, offset, args.filename)

pause = True
run = True
while run:
    clock.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                pause = not pause
            if event.key == pygame.K_s:
                Grid.save()
            if event.key == pygame.K_r:
                Grid.reset()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            Grid.HandleMouse(mouseX, mouseY)

    Grid.Conway(off_color=white, on_color=blue1, surface=screen, pause=pause)

    pygame.display.update()

pygame.quit()
