import pygame
import Main

grid = [[0 for x in range(Main.display_grid_width + 1)]
        for y in range(Main.display_grid_height + 1)]


def first_load(color=Main.morado):
    for column in range(Main.display_grid_width):
        for row in range(Main.display_grid_height):
            rect_pos_x = (
                Main.margen + (column * (Main.grid_width + Main.margen)))
            rect_pos_y = (
                Main.margen + (row * (Main.grid_height + Main.margen)))

            if grid[row][column] == 1:
                draw_rect(row, column, color)
            else:
                draw_rect(row, column, Main.blanco)
    return


def load_cursor(color=Main.morado, change=None):
    try:
        pos = pygame.mouse.get_pos()
        column = pos[0] // (Main.grid_width + Main.margen)
        row = pos[1] // (Main.grid_height + Main.margen)

        if change == None or (row, column) in change:
            if grid[row][column] == 1:
                draw_rect(row, column, color)
            else:
                draw_rect(row, column, Main.blanco)
        return
    except Exception:
        pass


def play(color=Main.morado):
    check = []
    for column in range(Main.display_grid_width):
        for row in range(Main.display_grid_height):
            alrededores = update(row, column)

            if alrededores <= 1:
                if grid[row][column] == 1:
                    check.append((row, column, 0))
            if alrededores == 3:
                if grid[row][column] == 0:
                    check.append((row, column, 1))
            if alrededores >= 4:
                if grid[row][column] == 1:
                    check.append((row, column, 0))

    for valor in check:
        grid[valor[0]][valor[1]] = valor[2]
        if valor[2] == 1:
            draw_rect(valor[0], valor[1], color)
        elif valor[2] == 0:
            draw_rect(valor[0], valor[1], Main.blanco)


def clean():
    for i in range(Main.display_grid_width):
        for j in range(Main.display_grid_height):
            if grid[i][j] == 1:
                grid[i][j] = 0
    first_load()


def update(x, y):
    sum = 0

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            sum = sum + grid[i % Main.display_grid_width][j %
                                                          Main.display_grid_height]

    return sum - grid[x][y]


def draw_rect(x, y, color):
    pygame.draw.rect(Main.gameDisplay, color, ((Main.margen + (y * (Main.grid_width + Main.margen))),
                     (Main.margen + (x * (Main.grid_height + Main.margen))), Main.grid_width, Main.grid_height), 0)
