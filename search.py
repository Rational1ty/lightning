from collections import deque
from typing import Optional

import graphics as g

from cell import Cell
from constants import ROWS
from grid import Grid


class BreadthFirstSearch:
	def __init__(self, grid: Grid, start: Cell, win: g.GraphWin):
		self.grid = grid
		self.window = win

		self.visited = set()
		self.q = deque([start])

		self.start = start
	
		self.first = True

	def next_front(self) -> list[Cell]:
		# if this is the first call
		if self.first:
			self.first = False
			return [self.start]

		front = []

		while len(self.q) > 0:
			curr = self.q.popleft()

			if curr in self.visited: continue
			self.visited.add(curr)

			adj = curr.getadjacent(self.grid)
			front.extend(adj)

		self.q = deque(front)
		return front




class DepthFirstSearch:
	...
