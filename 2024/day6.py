from collections import Counter

with open("day6.in", "r") as f:
    lab = {x + 1j * y: cell for y, row in enumerate(f) for x, cell in enumerate(row)}
    start = next(pos for pos, cell in lab.items() if cell == "^")
    up = 0 - 1j

def path(lab, position=start, velocity=up):
    while position in lab:
        yield position, velocity
        while lab.get(position + velocity) == "#":
            velocity *= 1j # turn right
        position += velocity

def loops(it):
    seen = set()
    for item in it:
        if item in seen:
            return True
        seen.add(item)
    return False

steps = set(pos for pos, vel in path(lab))
print(len(steps))
print(sum(1 for step in steps if lab[step] != "^" and loops(path({**lab, step: "#"}))))
