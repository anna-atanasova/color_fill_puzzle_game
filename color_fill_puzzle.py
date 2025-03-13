# Импортирање на отребните библиотеки
import pygame
import sys
from pygame.locals import *

# Иницијализација на Pygame
pygame.init()

# Константи
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 5
CELL_SIZE = WIDTH // GRID_SIZE
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]  # Red, Green, Blue, Yellow
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Setup на екранот
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Fill Puzzle ^_^")

# Game board
board = [[-1 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Фонт на инструкциите
font = pygame.font.Font(None, 36)

def draw_grid():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            color = WHITE if board[row][col] == -1 else COLORS[board[row][col]]
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, BLACK, rect, 2)

def is_valid_color(row, col, color_index):
    """Check if the color is valid or not"""
    neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    for r, c in neighbors:
        if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE:
            if board[r][c] == color_index:
                return False
    return True

def main():
    running = True
    selected_color = 0
    while running:
        screen.fill(WHITE)
        draw_grid()

        instructions = font.render("Click to fill cells. Avoid same colors in neighbors!", True, BLACK)
        screen.blit(instructions, (10, HEIGHT - 40))

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_1:
                    selected_color = 0
                elif event.key == K_2:
                    selected_color = 1
                elif event.key == K_3:
                    selected_color = 2
                elif event.key == K_4:
                    selected_color = 3
            elif event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                col, row = x // CELL_SIZE, y // CELL_SIZE

                if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
                    if is_valid_color(row, col, selected_color):
                        board[row][col] = selected_color

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
