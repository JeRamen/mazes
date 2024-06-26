from mazes.maze_generators.base_maze import Cell, Maze

import os
from pathlib import Path

# size of each cell in px
cell_size = 36
half = cell_size / 2
third = cell_size / 3
quarter = cell_size / 4
three_quarter = quarter * 3


class SVGCell:
    """
    Represents a square with fixed height and width provided in 'cell_size'.

    You can find more about SVG Path documentation here:
    https://www.w3schools.com/graphics/svg_path.asp
    """

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

        self.d = ""

        self.x = cell.x
        self.y = cell.y
        self.cell_type = cell.cell_type or cell.set_cell_type()

        # left upper corner coordinate
        self.luc = (self.x * cell_size, self.y * cell_size)

    def svg_path(self):
        return f"""
        <path 
                    stroke-opacity="{self.stroke_opacity}" 
                    stroke-width="{self.stroke_width}" 
                    stroke="{self.stroke_color}" 
                    fill="{self.fill}" 
                    d="{self.d}"
                />
        """

    # M = moveto (move from one point to another point)
    def dm(self, x_shift: float, y_shift: float):
        self.d += f"M {self.luc[0] + x_shift},{self.luc[1] + y_shift} \n"

    # L = lineto (create a line)
    def dl(self, x_shift: float, y_shift: float):
        self.d += f"L {self.luc[0] + x_shift},{self.luc[1] + y_shift} \n"

    # C = curveto (create a curve)
    def dc(
        self,
        x_start_curve_shift: float,
        y_start_curve_shift: float,
        x_end_curve_shift: float,
        y_end_curve_shift: float,
        x_end_shift: float,
        y_end_shift: float,
    ):
        self.d += (
            f"C {self.luc[0] + x_start_curve_shift},{self.luc[1] + y_start_curve_shift}"
            f" {self.luc[0] + x_end_curve_shift},{self.luc[1] + y_end_curve_shift}"
            f" {self.luc[0] + x_end_shift},{self.luc[1] + y_end_shift}\n"
        )

    # A = elliptical Arc (create a elliptical arc)
    def da(
        self,
        rx: float,
        ry: float,
        angle: float,
        large_arc_flag: int,
        sweep_flag: int,
        x_end_shift: float,
        y_end_shift: float,
    ):
        self.d += (
            f"A {rx} {ry}"
            f" {angle} {large_arc_flag} {sweep_flag}"
            f" {self.luc[0]+ x_end_shift},{self.luc[1] + y_end_shift}\n"
        )

    def render(self):
        match self.cell_type:
            case "l":
                self.type_l()

        return self.svg_path()

    def type_l(self):
        """
        l: ──┐
           ──┘
        """

        self.dm(x_shift=0, y_shift=quarter)
        self.dc(
            x_start_curve_shift=quarter,
            y_start_curve_shift=quarter,
            x_end_curve_shift=third,
            y_end_curve_shift=quarter / 2,
            x_end_shift=half,
            y_end_shift=quarter / 2,
        )
        self.da(
            rx=three_quarter / 2,
            ry=three_quarter / 2,
            angle=0,
            large_arc_flag=0,
            sweep_flag=1,
            x_end_shift=half,
            y_end_shift=quarter * 7 / 2,
        )
        self.dm(x_shift=0, y_shift=three_quarter)
        self.dc(
            x_start_curve_shift=quarter,
            y_start_curve_shift=three_quarter,
            x_end_curve_shift=third,
            y_end_curve_shift=quarter * 7 / 2,
            x_end_shift=half,
            y_end_shift=quarter * 7 / 2,
        )


def render_maze_to_svg(maze: Maze):
    svg_maze = [
        [SVGCell(cell=maze.maze_[y][x]) for x in range(maze.n)] for y in range(maze.m)
    ]

    view_box = max(maze.n, maze.m) * cell_size
    svg_cells_code = ""

    for svg_m_line in svg_maze:
        for svg_c in svg_m_line:
            svg_cells_code += svg_c.render()

    svg_code = f"""
        <svg   
            viewBox="0 0 {view_box} {view_box}" 
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink" 
            height="{maze.m * cell_size}" 
            width="{maze.n * cell_size}"
        >
            {svg_cells_code} 
        </svg>
    """

    dir_path = Path(__file__).parent.resolve() / "svg"

    os.makedirs(dir_path, exist_ok=True)

    with open(
        str(dir_path / f"svg_maze_({maze.n}x{maze.m}).svg"), "w", encoding="utf-8"
    ) as file:
        file.write(svg_code)
