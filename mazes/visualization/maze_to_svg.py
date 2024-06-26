from mazes.maze_generators.base_maze import Cell

# size of each cell in px
cell_size = 36
half = cell_size / 2
third = cell_size / 3
quarter = cell_size / 4
three_quarter = quarter * 3


class SVGCell:
    def __init__(
        self,
        cell: Cell,
        stroke_opacity: float = 1,
        stroke_width: float = 2,
        stroke_color: str = "black",
        fill: str = "none",
    ) -> None:
        self.stroke_opacity = stroke_opacity
        self.stroke_width = stroke_width
        self.stroke_color = stroke_color
        self.fill = fill

        self.svg_path = ""
        self.d = ""

        self.x = cell.x
        self.y = cell.y
        self.cell_type = cell.cell_type or cell.set_cell_type()

        # left upper corner coordinate
        self.luc = (self.x * cell_size, self.y * cell_size)
