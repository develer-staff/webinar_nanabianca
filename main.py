import os

import pygame

import grid

os.environ["SDL_VIDEO_CENTERED"] = "1"

# resolution
width, height = 1920, 1080
size = (width, height)

pygame.init()
pygame.display.set_caption("CONWAY'S GAME OF LIFE")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 10
font = pygame.font.SysFont("Arial", 30)

black = (0, 0, 0)
blue = (0, 121, 150)
blue1 = (0, 14, 71)
white = (255, 255, 255)

scaler = 30
offset = 1

Grid = grid.Grid(width, height, scaler, offset)
Grid.random2d_array()

pause = False
run = True


def drawFpsLabel(fps, font):
    label = font.render(str(fps), 1, (255, 0, 0))
    screen.blit(label, (30, 30))


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
            if event.key == pygame.K_LEFT:
                fps -= 5
            if event.key == pygame.K_RIGHT:
                fps += 5

    Grid.Conway(off_color=white, on_color=blue1, surface=screen, pause=pause)
    drawFpsLabel(fps, font)

    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        Grid.HandleMouse(mouseX, mouseY)

    pygame.display.update()

pygame.quit()
