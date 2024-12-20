with open("day20.in", "r") as f:
    grid = {x + 1j * y: cell for y, row in enumerate(f) for x, cell in enumerate(row)}

pos = next(pos for pos, cell in grid.items() if cell == "S")
end = next(pos for pos, cell in grid.items() if cell == "E")
path = {pos: 0}
while end not in path:
    pos = next(
        pos + step
        for step in [1, 1j, -1, -1j]
        if grid[pos + step] != "#" and pos + step not in path
    )
    path[pos] = len(path)

def steps(pos, limit):
    for dy in range(-limit, limit + 1):
        for dx in range(-limit + abs(dy), limit + 1 - abs(dy)):
            yield dx + 1j * dy

def saves100(pos, step):
    return path.get(pos + step, 0) >= path[pos] + 100 + abs(step.real) + abs(step.imag)

print(sum(1 for pos in path for step in steps(pos, 2) if saves100(pos, step)))
print(sum(1 for pos in path for step in steps(pos, 20) if saves100(pos, step)))
