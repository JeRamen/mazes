from random import shuffle

from mazes.maze_generators.base_maze import Cell, opposite_

visited = []


def rdfs_parse(current_cell: Cell):
    visited.append(current_cell)

    possible_moves = list(current_cell.neighbours.keys())
    shuffle(possible_moves)

    for move in possible_moves:
        if current_cell.neighbours[move] in visited:
            continue

        new_cell = current_cell.neighbours[move]
        current_cell.walls[move] = False
        new_cell.walls[opposite_[move]] = False

        rdfs_parse(new_cell)
