import ctypes
from math import floor

from graphics import color_rgb

# system 
SCREEN_WIDTH = ctypes.windll.user32.GetSystemMetrics(0)
SCREEN_HEIGHT = ctypes.windll.user32.GetSystemMetrics(1)

# window, cells, and grid
MAX_WIDTH = 1200
MAX_HEIGHT = 700
CELL_SIZE = 15
CELL_PADDING = 2
WIDTH = floor(MAX_WIDTH / CELL_SIZE) * CELL_SIZE
HEIGHT = floor(MAX_HEIGHT / CELL_SIZE) * CELL_SIZE
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE
POS_X = (SCREEN_WIDTH - WIDTH) // 2
POS_Y = 0

assert CELL_PADDING * 2 < CELL_SIZE, 'Cell padding too large'

# colors
BG_COLOR = color_rgb(30, 30, 30)
FG_COLOR = color_rgb(100, 100, 100)

# # yellow
# HIGHLIGHT = (
# 	color_rgb(240, 240, 120),
# 	color_rgb(160, 160, 80),
# 	color_rgb(80, 80, 40),
# )

# blue
HIGHLIGHT = (
	color_rgb(150, 235, 255),
	color_rgb(100, 175, 195),
	color_rgb(60, 100, 110)
)

# timing
REFRESH_RATE = 15
STRIKE_FADE_RATE = len(HIGHLIGHT) * 30 / 4
STRIKE_PROP_RATE = 0

# probability
PROB_VERT = 0.5
PROB_HORIZ = 0.25

# options
SHOW_GRID = True
FADE_CELLS = True
MULTIPLE_STARTS = True
N_STARTS = 3
