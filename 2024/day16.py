from heapq import heappush, heappop, heapify
from dataclasses import dataclass, field

@dataclass(order=True)
class Entry:
    dist: int
    node: any=field(compare=False)
    prev: any=field(compare=False)

def shortestpaths(edges, start):
    dist = dict()
    prev = dict()
    frontier = [Entry(0, v, None) for v in start]
    heapify(frontier)
    while frontier:
        entry = heappop(frontier)
        d, v, p = entry.dist, entry.node, entry.prev
        if v in prev:
            if d == dist[v]:
                prev[v].add(p)
            continue
        dist[v] = d
        prev[v] = {p}
        for u, ud in edges.get(v, dict()).items():
            heappush(frontier, Entry(d + ud, u, v))
    return dist, prev

with open("day16.in", "r") as f:
    grid = {x + 1j * y: cell for y, row in enumerate(f) for x, cell in enumerate(row)}
    start = next(pos for pos, cell in grid.items() if cell == "S")
    end = next(pos for pos, cell in grid.items() if cell == "E")
    grid[start] = "."
    grid[end] = "."
    starts = [start + 0.25]
    ends = [end + step * 0.25 for step in [1, 1j, -1, -1j]]

edges = {
    pos + step * 0.25: {
        pos + step + step * 0.25: 1,
        pos + step * 0.25j: 1000,
        pos + step * -0.25j: 1000,
    }
    for pos in grid
    for step in [1, 1j, -1, -1j]
    if grid[pos] == "."
}

dist, prev = shortestpaths(edges, starts)
d, end = min((dist[end], end) for end in ends if end in dist)
print(d)

seats = set()
todo = {end}
while todo:
    seats.update(todo)
    todo = {p for node in todo for p in prev.get(node, set()) if p} - seats
seats = {round(seat.real) + round(seat.imag) * 1j for seat in seats}
print(len(seats))
