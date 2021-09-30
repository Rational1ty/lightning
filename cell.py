from random import random

import graphics as g

from constants import *
from grid import Grid


class Cell:
	HL_MAX = len(HIGHLIGHT)
	HL_OFF = 0

	def __init__(self, row: int, col: int):
		self.row = row
		self.col = col

		self.start = g.Point(col * CELL_SIZE, row * CELL_SIZE)
		self.end = g.Point(self.start.x + CELL_SIZE, self.start.y + CELL_SIZE)

		self.top = random() < PROB_HORIZ
		self.left = random() < PROB_VERT

		self.highlight = 0
		self.rect = g.Rectangle(
			g.Point(self.start.x + CELL_PADDING, self.start.y + CELL_PADDING),
			g.Point(self.end.x - CELL_PADDING, self.end.y - CELL_PADDING)
		)

		self.parent = None

	@staticmethod
	def backtrack(start: 'Cell') -> list['Cell']:
		path = [start]
		curr = start
		
		while curr.parent is not None:
			path.append(curr.parent)
			curr = curr.parent

		return path

	def getadjacent(self, grid: Grid['Cell']) -> list['Cell']:
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

	def setcolor(self, color: str, window: g.GraphWin = None):
		if color is None:
			self.rect.undraw()
			return

		assert window is not None, 'Must provide argument for `window` when setting color'

		self.rect.setFill(color)
		self.rect.setOutline(color)

		try:
			self.rect.draw(window) 
		except g.GraphicsError:
			pass

	def sethighlight(self, hl: int, window: g.GraphWin = None):
		self.highlight = hl

		if hl == Cell.HL_OFF:
			self.rect.undraw()
			return

		assert window is not None, 'Must provide argument for `window` when setting highlight'

		color = self._getcolor(hl)

		self.rect.setFill(color)
		self.rect.setOutline(color)

		try:
			self.rect.draw(window) 
		except g.GraphicsError:
			pass

	def _getcolor(self, hl: int) -> str:
		return HIGHLIGHT[Cell.HL_MAX - hl]

	def __repr__(self) -> str:
		return f'Cell({self.row}, {self.col})'
