from collections import deque

from cell import Cell
from grid import Grid


class BreadthFirstSearch:
	def __init__(self, grid: Grid[Cell], *start: Cell):
		self.grid = grid

		self.visited = set()
		self.q = deque(start)

		self.start = start
		self.first = True

	def next_front(self) -> list[Cell]:
		# return starting cells on first call
		if self.first:
			self.first = False
			return list(self.start)

		front = []

		while len(self.q) > 0:
			curr = self.q.popleft()

			if curr in self.visited: continue
			self.visited.add(curr)

			adj = curr.getadjacent(self.grid)

			# set parent of adjacent cells to current cell
			for cell in adj:
				if cell in self.visited: continue
				if cell.parent is not None: continue
				cell.parent = curr

			front.extend(adj)

		self.q = deque(front)
		return front
