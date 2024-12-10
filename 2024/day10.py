from collections import defaultdict, Counter

with open("day10.in", "r") as f:
    heights = {x + y * 1j: int(h) for y, row in enumerate(f) for x, h in enumerate(row.strip())}

trailheads = {pos: Counter([pos]) for pos, h in heights.items() if h == 0}
for _ in range(9):
    new_trailheads = defaultdict(Counter)
    for pos, heads in trailheads.items():
        for step in [1, 1j, -1, -1j]:
            if heights.get(pos + step) == heights[pos] + 1:
                new_trailheads[pos + step].update(heads)
    trailheads = new_trailheads

print(sum(len(heads) for heads in trailheads.values()))
print(sum(heads.total() for heads in trailheads.values()))
