from collections import Counter

with open("day10.in", "r") as f:
    heights = {x + y * 1j: int(h) for y, row in enumerate(f) for x, h in enumerate(row.strip())}

trailheads = {pos: Counter([pos]) for pos, h in heights.items() if h == 0}
for height in range(1, 10):
    trailheads = {
        pos: sum((trailheads.get(pos + d, Counter()) for d in [1, 1j, -1, -1j]), start=Counter())
        for pos, h in heights.items() if h == height
    }

print(sum(len(heads) for heads in trailheads.values()))
print(sum(heads.total() for heads in trailheads.values()))
