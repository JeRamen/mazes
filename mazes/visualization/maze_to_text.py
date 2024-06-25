from mazes.maze_generators.base_maze import Maze

import os
from pathlib import Path

"""
CELL TYPES:
    L: ──┐
       ──┘
    R: ┌──
       └──
    U: │ │
       └─┘
    D: ┌─┐
       │ │
    LR: ───
        ───
    LU: ┘ │
        ──┘
    LD: ──┐
        ┐ │
    RU: │ └
        └──
    RD: ┌──
        │ ┌
    UD: │ │
        │ │
    LRU: ┘ └
         ───
    LRD: ───
         ┐ ┌
    LUD: ┘ │
         ┐ │
    RUD: │ └
         │ ┌
    LRUD: ┘ └
          ┐ ┌
"""

CELL_TYPES = {
    "l": ("──┐", "──┘"),
    "r": ("┌──", "└──"),
    "u": ("│ │", "└─┘"),
    "d": ("┌─┐", "│ │"),
    "lr": ("───", "───"),
    "lu": ("┘ │", "──┘"),
    "ld": ("──┐", "┐ │"),
    "ru": ("│ └", "└──"),
    "rd": ("┌──", "│ ┌"),
    "ud": ("│ │", "│ │"),
    "lru": ("┘ └", "───"),
    "lrd": ("───", "┐ ┌"),
    "lud": ("┘ │", "┐ │"),
    "rud": ("│ └", "│ ┌"),
    "lrud": ("┘ └", "┐ ┌"),
}


def maze_to_text(maze: Maze, print_cli: bool = True, export: bool = False):
    assert maze
    assert maze.maze_

    text_maze = ""

    for m_line in maze.maze_:
        m_line_cell_types = [c.cell_type or c.set_cell_type() for c in m_line]
        text_maze += "".join([CELL_TYPES[ct][0] for ct in m_line_cell_types])
        text_maze += "\n"
        text_maze += "".join([CELL_TYPES[ct][1] for ct in m_line_cell_types])
        text_maze += "\n"

    if print_cli:
        print(text_maze)

    if export:
        dir_path = Path(__file__).parent.resolve() / "txt"

        os.makedirs(dir_path, exist_ok=True)

        with open(
            str(dir_path / f"text_maze_({maze.n}x{maze.m})"), "w", encoding="utf-8"
        ) as file:
            file.write(text_maze.strip())
