from typing import Dict

opposite_ = {
    "l": "r",
    "r": "l",
    "u": "d",
    "d": "u",
}


class Cell:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.neighbours: Dict[str, Cell] = {}
        self.walls = {
            "l": True,
            "r": True,
            "u": True,
            "d": True,
        }

        self.cell_type = ""

    def __repr__(self) -> str:
        return f"({self.x},{self.y})"

    def __eq__(self, value: object, /) -> bool:
        if isinstance(value, Cell):
            return self.x == value.x and self.y == value.y

        return False

    def set_cell_type(self):
        self.cell_type = "".join([wk for wk, val in self.walls.items() if not val])

        return self.cell_type


class Maze:
    def __init__(self, n: int, m: int) -> None:
        self.n = n
        self.m = m

        self.maze_ = [[Cell(x, y) for x in range(n)] for y in range(m)]

        self.set_cell_neighbours()

    def print_m(self) -> None:
        for m_line in self.maze_:
            for c in m_line:
                print(c, end="")
            print()

    def check_shifts(self, shifts: Dict) -> Dict:
        shifts_checked = {}

        for shift_dir, new_cell_coor in shifts.items():
            if new_cell_coor[0] < 0 or new_cell_coor[1] < 0:
                continue

            if new_cell_coor[0] > self.n - 1 or new_cell_coor[1] > self.m - 1:
                continue

            shifts_checked[shift_dir] = new_cell_coor

        return shifts_checked

    def get_shifts(self, cell: Cell) -> Dict:
        shifts = {
            "l": (cell.x - 1, cell.y),  # left
            "r": (cell.x + 1, cell.y),  # right
            "u": (cell.x, cell.y - 1),  # up
            "d": (cell.x, cell.y + 1),  # down
        }
        return self.check_shifts(shifts)

    def set_cell_neighbours(self):
        for m_line in self.maze_:
            for c in m_line:
                new_cell_coors = self.get_shifts(c)
                c.neighbours = {
                    k: self.maze_[v[1]][v[0]] for k, v in new_cell_coors.items()
                }
