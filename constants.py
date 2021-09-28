from math import floor
import ctypes
from graphics import color_rgb

# system 
SCREEN_WIDTH = ctypes.windll.user32.GetSystemMetrics(0)
SCREEN_HEIGHT = ctypes.windll.user32.GetSystemMetrics(1)

# window, cells, and grid
MAX_WIDTH = 1000
MAX_HEIGHT = 700
CELL_SIZE = 20
CELL_PADDING = 2
WIDTH = floor(MAX_WIDTH / CELL_SIZE) * CELL_SIZE
HEIGHT = floor(MAX_HEIGHT / CELL_SIZE) * CELL_SIZE
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE
POS_X = (SCREEN_WIDTH - WIDTH) // 2
POS_Y = 0

assert CELL_PADDING * 2 < CELL_SIZE, 'Cell padding too large'

# timing
REFRESH_RATE = 10
STRIKE_FADE_RATE = 20
STRIKE_PROP_RATE = 0

# colors
BG_COLOR = color_rgb(30, 30, 30)
FG_COLOR = color_rgb(100, 100, 100)
HIGHLIGHT_1 = color_rgb(240, 240, 120)
HIGHLIGHT_2 = color_rgb(160, 160, 80)
HIGHLIGHT_3 = color_rgb(80, 80, 40)
HIGHLIGHT_SPECIAL = color_rgb(40, 210, 255)

# probability
PROB_VERT = 0.5
PROB_HORIZ = 0.25

# options
SHOW_GRID = True