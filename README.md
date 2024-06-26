## App to generate and visualize mazes 

### Generating mazes

#### Randomized depth-first-search

Recursive backtracker. Is implemented using recursive approach. Start with randomly selected cell:

```python
start_cell = maze.maze_[0][0]
rdfs_parse(start_cell)
```

mark the cell as visited:

```python
visited.append(current_cell)
```

if the cell has any unvisited neighbours:

```python
possible_moves = list(current_cell.neighbours.keys())
```

randomly select one of unvisited neighbours:

```python
shuffle(possible_moves)
for move in possible_moves:
    if current_cell.neighbours[move] in visited:
        continue
```

remove wall between the cell and its neighbour:

```python
new_cell = current_cell.neighbours[move]
current_cell.walls[move] = False
new_cell.walls[opposite_[move]] = False
```

invoke parser again with neighbour as argument:

```python
rdfs_parse(new_cell)
```

In the end you will have set walls for every cell and visited stack, which
is basically a path cursor built.

### Visualizing mazes

#### Text based visualizer

Having cell type, which represents cell open walls: 

```python
['l', 'r', ..., 'ru', 'rd', ..., 'lru', 'lrd', ..., 'lrud']
```

we can callate cell type with ascii representation:

```python
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
```

and then just substitute:

```python
for m_line in maze.maze_:
    m_line_cell_types = [c.cell_type or c.set_cell_type() for c in m_line]
    text_maze += "".join([CELL_TYPES[ct][0] for ct in m_line_cell_types])
    text_maze += "\n"
    text_maze += "".join([CELL_TYPES[ct][1] for ct in m_line_cell_types])
    text_maze += "\n"
```

#### SVG visualizer

The same as with text visualizer, having cell type, we can draw each cell separately, using SVG Path
'd' attribute, with 'M', 'L', 'C' and 'A' path commands.
