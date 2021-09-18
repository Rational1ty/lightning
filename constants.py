from math import floor

from graphics import color_rgb

# window constants
MAX_WIDTH = 1000
MAX_HEIGHT = 600
CELL_SIZE = 25
WIDTH = floor(MAX_WIDTH / CELL_SIZE) * CELL_SIZE
HEIGHT = floor(MAX_HEIGHT / CELL_SIZE) * CELL_SIZE
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

# colors
BG_COLOR = color_rgb(30, 30, 30)
FG_COLOR = color_rgb(200, 200, 200)
HIGHLIGHT_1 = color_rgb(255, 255, 185)
HIGHLIGHT_2 = color_rgb(255, 255, 205)
HIGHLIGHT_3 = color_rgb(255, 255, 225)

# probability
PROB_VERT = 0.5
PROB_HORIZ = 0.25