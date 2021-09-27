import itertools as it
from search import BreadthFirstSearch
from time import sleep
from typing import Generator

import graphics as g

from cell import Cell
from constants import BG_COLOR, COLS, FG_COLOR, HEIGHT, HIGHLIGHT_SPECIAL, REFRESH_RATE, ROWS, WIDTH
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
			line.draw(window)

		if cell.left:
			line = g.Line(cell.start, pt(cell.start.x, cell.end.y))
			line.setFill(FG_COLOR)
			line.draw(window)
	g.update()


def update_highlights(visited: set[Cell], window: g.GraphWin):
	for cell in visited:
		if cell.highlight > Cell.HL_OFF:
			cell.sethighlight(cell.highlight - 1, window)


def clear_highlights(grid: Grid):
	for cell in grid:
		cell: Cell
		cell.sethighlight(Cell.HL_OFF)


# def dfs(grid: Grid, window: g.GraphWin, start: Cell, visited: set[Cell]) -> Union[Cell, None]:
# 	if start.row == ROWS - 1:
# 		return start

# 	if start in visited: return None

# 	visited.add(start)
# 	start.sethighlight(Cell.HL_HIGH, window)
# 	sleep(0.05)

# 	adj = start.getadjacent(grid)

# 	for cell in adj:
# 		res = dfs(grid, window, cell, visited)
# 		if res is None: continue
# 		return res

# 	return None

def main():
	window = g.GraphWin('Lightning', WIDTH, HEIGHT, autoflush=False)
	window.setBackground(BG_COLOR)
	window.toScreen(0, 0)

	grid = Grid(ROWS, COLS, *get_cells())

	draw_gridlines(window, grid)

	start: Cell = grid[0, COLS // 2]

	bfs = BreadthFirstSearch(grid, start)
	done = False
	end = None

	sleep(1)

	while not done:
		update_highlights(bfs.visited, window)

		front = bfs.next_front()

		if len(front) == 0:
			done = True

		for cell in front:
			cell.sethighlight(Cell.HL_HIGH, window)
			
			if cell.row == ROWS - 1:
				done = True
				end = cell

		g.update(REFRESH_RATE)
		
	# display path
	sleep(1)
	clear_highlights(grid)

	path = Cell.backtrack(end)
	for cell in path:
		cell.sethighlight(Cell.HL_HIGH, window)

	start.setcolor(HIGHLIGHT_SPECIAL, window)
	end.setcolor(HIGHLIGHT_SPECIAL, window)
	
	g.update()
	sleep(2)

	window.close()


if __name__ == '__main__':
	main()
