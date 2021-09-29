import itertools as it
import random
from time import sleep
from typing import Generator

import graphics as g

from cell import Cell
from constants import *
from grid import Grid
from search import BreadthFirstSearch


def pt(x: int, y: int) -> g.Point:
	return g.Point(x, y)


def get_cells() -> Generator[Cell, None, None]:
	yield from (Cell(r, c) for r, c in it.product(range(ROWS), range(COLS)))


def get_start(grid: Grid[Cell]) -> tuple[Cell, ...]:
	n = N_STARTS if MULTIPLE_STARTS else 1
	return random.sample(list(grid[0:1]), n)


def draw_gridlines(window: g.GraphWin, grid: Grid[Cell]):
	for cell in grid:
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


def clear_highlights(grid: Grid[Cell]):
	for cell in grid:
		cell.sethighlight(Cell.HL_OFF)


def strike(cells: set[Cell], window: g.GraphWin, times: int = 2):
	for _ in range(times):
		for cell in cells:
			cell.sethighlight(Cell.HL_MAX, window)
		g.update()
		
		for __ in range(Cell.HL_MAX):
			update_highlights(cells, window)
			g.update(STRIKE_FADE_RATE)


def play_strike_sequence(cells: list[Cell], grid: Grid[Cell], window: g.GraphWin):
	sleep(0.1)
	clear_highlights(grid)

	for cell in cells:
		cell.sethighlight(Cell.HL_MAX, window)
		g.update(STRIKE_PROP_RATE)

	strike(set(cells), window)
	sleep(0.01)
	strike(set(cells), window, 1)

	for cell in cells:
		cell.sethighlight(Cell.HL_MAX, window)

	g.update()


def main():
	window = g.GraphWin('Lightning', WIDTH, HEIGHT, autoflush=False)
	window.setBackground(BG_COLOR)
	window.master.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')

	grid = Grid(ROWS, COLS, *get_cells())

	if SHOW_GRID:
		draw_gridlines(window, grid)

	start = get_start(grid)

	bfs = BreadthFirstSearch(grid, *start)
	done = False
	end = None

	sleep(1)

	while not done:
		front = bfs.next_front()

		if len(front) == 0:
			exit(0)

		for cell in front:
			if cell.row == ROWS - 1:
				done = True
				end = cell
			cell.sethighlight(Cell.HL_MAX, window)

		if FADE_CELLS:
			update_highlights(bfs.visited, window)
		g.update(REFRESH_RATE)

	path = Cell.backtrack(end)
	play_strike_sequence(path, grid, window)
	
	window.getKey()


if __name__ == '__main__':
	main()
