from mazes.maze_generators.base_maze import Maze
from mazes.maze_generators.rdfs_recursive import rdfs_parse

from mazes.visualization.maze_to_text import maze_to_text
from mazes.visualization.maze_to_svg import render_maze_to_svg


if __name__ == "__main__":
    maze = Maze(25, 25)

    start_cell = maze.maze_[0][0]

    rdfs_parse(start_cell)

    maze_to_text(maze, export=True)

    render_maze_to_svg(maze)
