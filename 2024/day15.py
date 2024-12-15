with open("day15.in", "r") as f:
    rows, moves = [block.splitlines() for block in f.read().split("\n\n")]
    directions = {"^": -1j, ">": 1, "v": 1j, "<": -1}
    moves = [directions[move] for line in moves for move in line]

class Grid:
    def __init__(self, rows):
        self.grid = {x + 1j * y: cell for y, row in enumerate(rows) for x, cell in enumerate(row)}
        self.robot = next(pos for pos, cell in self.grid.items() if cell == "@")
        self.grid[self.robot] = " "
        self.boxcount = sum(1 for cell in self.grid.values() if cell in "[O")

    def move(self, move):
        pushed = set()
        frontier = {self.robot}
        while frontier:
            if any(self.grid[pos + move] == "#" for pos in frontier):
                return
            frontier = {pos + move for pos in frontier if self.grid[pos + move] in "[O]"}
            boxmap = {"[": 1, "]": -1}
            frontier |= {pos + boxmap[self.grid[pos]] for pos in frontier if self.grid[pos] in boxmap}
            frontier -= pushed
            pushed |= frontier
        override = {pos: " " for pos in pushed}
        override.update({pos + move: self.grid[pos] for pos in pushed})
        self.grid.update(override)
        self.robot += move

    def render(self):
        height = round(max(pos.imag for pos in self.grid)) + 1
        width = round(max(pos.real for pos in self.grid)) + 1
        for y in range(height):
            print("".join("@" if self.robot == x + 1j * y else self.grid[x + 1j * y] for x in range(width)))

    def gps(self):
        return round(sum(100 * pos.imag + pos.real for pos, cell in self.grid.items() if cell in "[O"))

tilemap = {"#": "##", "O": "[]", ".": "  ", "@": "@ "}
grids = [
    Grid([row.replace(".", " ") for row in rows]),
    Grid(["".join(tilemap[cell] for cell in row) for row in rows]),
]
for grid in grids:
    for move in moves:
        grid.move(move)
    print(grid.gps())
