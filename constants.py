from math import floor

from graphics import color_rgb

# window constants
MAX_WIDTH = 1000
MAX_HEIGHT = 600
CELL_SIZE = 20
WIDTH = floor(MAX_WIDTH / CELL_SIZE) * CELL_SIZE
HEIGHT = floor(MAX_HEIGHT / CELL_SIZE) * CELL_SIZE
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

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


def gethighlightcolor(level: int) -> str:
	# MAX_RGB = 200, 200, 100
	INC_RGB = 80, 80, 40
	rgb = tuple(level * comp for comp in INC_RGB)
	return color_rgb(*rgb)


# probability
PROB_VERT = 0.5
PROB_HORIZ = 0.25