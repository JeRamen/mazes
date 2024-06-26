from random import choice

from mazes.maze_generators.base_maze import Cell, opposite_

stack = []
visited = []


def rdfs_iter(current_cell: Cell):
    stack.append(current_cell)
    visited.append(current_cell)

    while stack:
        current_cell = stack.pop()

        possible_moves = {
            dir: cell
            for dir, cell in current_cell.neighbours.items()
            if cell not in visited
        }

        if not possible_moves:
            continue

        stack.append(current_cell)

        new_cell = choice(list(possible_moves.items()))

        stack.append(new_cell[1])
        visited.append(new_cell[1])

        current_cell.walls[new_cell[0]] = False
        new_cell[1].walls[opposite_[new_cell[0]]] = False
