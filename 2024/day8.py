from collections import defaultdict
from itertools import permutations

with open("day8.in", "r") as f:
    grid = f.read().splitlines()
    height = len(grid)
    width = len(grid[0])

antennas = defaultdict(set)
for y, row in enumerate(grid):
    for x, freq in enumerate(row):
        if freq != ".":
            antennas[freq].add(x + y * 1j)

def antinodes(harmonics):
    for freq, positions in antennas.items():
        for (pos1, pos2) in permutations(positions, 2):
            for h in harmonics:
                antinode = pos1 + h * (pos1 - pos2)
                if not (0 <= antinode.real < width and 0 <= antinode.imag < height):
                    break
                yield antinode

print(len(set(antinodes([1]))))
print(len(set(antinodes(range(max(width, height))))))
