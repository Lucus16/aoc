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

def antinodes(resonant_harmonics):
    for freq, positions in antennas.items():
        for (pos1, pos2) in permutations(positions, 2):
            if resonant_harmonics:
                yield pos1
            antinode = pos1 + pos1 - pos2
            while 0 <= antinode.real < width and 0 <= antinode.imag < height:
                yield antinode
                if not resonant_harmonics:
                    break
                antinode += pos1 - pos2

print(len(set(antinodes(False))))
print(len(set(antinodes(True))))
