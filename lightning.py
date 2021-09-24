import itertools as it
from collections import deque
from time import sleep
from typing import Generator, Union

import graphics as g

from cell import Cell
from constants import BG_COLOR, COLS, FG_COLOR, HEIGHT, ROWS, WIDTH
from grid import Grid


def pt(x: int, y: int) -> g.Point:
	return g.Point(x, y)


def get_cells() -> Generator[Cell, None, None]:
	yield from (Cell(r, c) for r, c in it.product(range(ROWS), range(COLS)))


def draw_gridlines(window: g.GraphWin, grid: Grid):
	for cell in grid:
		cell: Cell

		if cell.top:
			line = g.Line(cell.start, pt(cell.end.x, cell.start.y))
			line.setFill(FG_COLOR)
			window.addItem(line)

		if cell.left:
			line = g.Line(cell.start, pt(cell.start.x, cell.end.y))
			line.setFill(FG_COLOR)
			window.addItem(line)

	window.redraw()


def bfs(grid: Grid, window: g.GraphWin, start: Cell) -> Union[Cell, None]:
	q = deque([start])
	visited = set()

	# while there are elements in the queue
	while len(q) > 0:
		curr = q.popleft()	# get first element from queue

		if curr in visited: continue

		curr.sethighlight(Cell.HL_HIGH, window)
		sleep(0.005)
		
		# get its neighbors
		adj = curr.getadjacent(grid)

		# check if adjacent cells have been visited or are at end
		for cell in adj:
			if cell in visited:
				adj.remove(cell)
				continue
			if cell.row == ROWS - 1:
				return cell

		visited.add(curr)	# current cell has been visited
		q.extend(adj)		# add adjacent cells to queue

	return None


def update_highlights(visited: set[Cell], window: g.GraphWin):
	for cell in visited:
		if cell.highlight > 0:
			cell.sethighlight(cell.highlight - 1, window)


def manhattan_dist(cell_1: Cell, cell_2: Cell) -> int:
	return abs(cell_1.row - cell_2.row) + abs(cell_1.col - cell_2.col)


def dfs(grid: Grid, window: g.GraphWin, start: Cell, visited: set[Cell]) -> Union[Cell, None]:
	if start.row == ROWS - 1:
		return start

	if start in visited: return None

	visited.add(start)
	start.sethighlight(Cell.HL_HIGH, window)
	sleep(0.05)

	adj = start.getadjacent(grid)

	for cell in adj:
		res = dfs(grid, window, cell, visited)
		if res is None: continue
		return res

	return None

def main():
	window = g.GraphWin('Graphics test', WIDTH, HEIGHT)
	window.setBackground(BG_COLOR)
	window.toScreen(0, 0)

	grid = Grid(ROWS, COLS, *get_cells())

	draw_gridlines(window, grid)

	start = grid[0, COLS // 2]

	sleep(1)
	(bfs(grid, window, start) or start).sethighlight(Cell.HL_HIGH, window)
	sleep(2)

	for cell in grid:
		cell: Cell
		cell.sethighlight(Cell.HL_OFF)

	sleep(1)
	(dfs(grid, window, start, set()) or start).sethighlight(Cell.HL_HIGH, window)
	sleep(2)

	window.close()


if __name__ == '__main__':
	main()
