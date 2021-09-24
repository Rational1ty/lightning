from random import random

from constants import CELL_SIZE, COLS, HIGHLIGHT_1, HIGHLIGHT_2, HIGHLIGHT_3, PROB_HORIZ, PROB_VERT, ROWS
from grid import Grid
import graphics as g


class Cell:
	HIGH = 3
	MED = 2
	LOW = 1
	OFF = 0

	def __init__(self, row: int, col: int):
		self.row = row
		self.col = col

		self.start = g.Point(col * CELL_SIZE, row * CELL_SIZE)
		self.end = g.Point(self.start.x + CELL_SIZE, self.start.y + CELL_SIZE)

		self.top = random() < PROB_HORIZ
		self.left = random() < PROB_VERT

		self.highlight = 0
		self.rect = g.Rectangle(
			g.Point(self.start.x + 5, self.start.y + 5),
			g.Point(self.end.x - 5, self.end.y - 5)
		)

	def getadjacent(self, grid: Grid) -> list['Cell']:
		r, c = self.row, self.col
		row_max = ROWS - 1
		col_max = COLS - 1

		# cells adjacent to edges (bottom, left, right, top)
		neighbors: list[Cell] = [
			grid[r + 1, c] if r < row_max else None,
			grid[r, c - 1] if c > 0 else None,
			grid[r, c + 1] if c < col_max else None,
			grid[r - 1, c] if r > 0 else None
		]

		# check for barriers between adjacent cells
		if neighbors[0] and neighbors[0].top:
			neighbors[0] = None
		if self.left:
			neighbors[1] = None
		if neighbors[2] and neighbors[2].left:
			neighbors[2] = None
		if self.top:
			neighbors[3] = None
		
		return list(filter(lambda c: c is not None, neighbors))

	def sethighlight(self, hl: int, window: g.GraphWin = None):
		self.highlight = hl

		if hl == Cell.OFF:
			self.rect.undraw()
			return

		assert window is not None, 'Must provide argument for `window` when setting highlight'

		color = self.getcolor(hl)

		self.rect.setFill(color)
		self.rect.setOutline(color)

		try:
			self.rect.draw(window) 
		except g.GraphicsError:
			pass

	def getcolor(self, hl: int) -> str:
		return \
			HIGHLIGHT_1 if hl == Cell.HIGH else \
			HIGHLIGHT_2 if hl == Cell.MED else \
			HIGHLIGHT_3 if hl == Cell.LOW else \
			None

	def __repr__(self) -> str:
		return f'Cell({self.row}, {self.col})'
