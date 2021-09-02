import pygame
import level
import time
import os
import random as rand

margen = 1
grid_width = 10
grid_height = 10
display_grid_width = 90   # Ancho en cuadrados
display_grid_height = 90  # Altura en cuadrados
display_width = (grid_width + margen) * display_grid_width + margen
display_height = (grid_height + margen) * display_grid_height + margen

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('El juego de la vida de Conway')
clock = pygame.time.Clock()

negro = (0, 0, 0)
blanco = (220, 220, 220)
morado = (134, 67, 174)

pygame.display.set_icon(pygame.image.load(os.path.dirname(
    os.path.abspath(__file__)) + "\Space_invader.png"))


def game_loop():
    rainbow = (rand.randint(30, 200), rand.randint(
        30, 200), rand.randint(30, 200))
    change = []
    Process = True
    Running = False
    last_grid = ('', '')
    level.first_load(rainbow)

    while Process:
        rainbow = ((rainbow[0] + rand.randint(5, 30)) % 255, (rainbow[1] +
                   rand.randint(5, 30)) % 255, (rainbow[2] + rand.randint(5, 30)) % 255)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Process = False
                Running = False
                return 0
            if pygame.mouse.get_pressed()[0]:
                try:
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // (grid_width + margen)
                    row = pos[1] // (grid_height + margen)

                    if (row, column) != last_grid:
                        if level.grid[row][column] == 0:
                            level.grid[row][column] = 1
                        else:
                            level.grid[row][column] = 0
                        last_grid = (row, column)
                        change.append((row, column))
                except MouseOutOfBounds:
                    pass

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    Running = True
                if event.key == pygame.K_DELETE:
                    level.clean()
        level.load_cursor(rainbow, change)
        change = []
        pygame.display.flip()
        clock.tick(500)

        while Running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Process = False
                    Running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        Process = True
                        Running = False
            rainbow = ((rainbow[0] + rand.randint(5, 30)) % 255, (rainbow[1] +
                       rand.randint(5, 30)) % 255, (rainbow[2] + rand.randint(5, 30)) % 255)
            level.play(rainbow)
            pygame.display.update()
            clock.tick(20)


if __name__ == '__main__':
    game_loop()
    pygame.quit()
    quit()
