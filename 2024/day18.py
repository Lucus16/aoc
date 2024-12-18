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

with open("day18.in", "r") as f:
    lines = [line.split(",") for line in f]
    corruptions = [int(x) + int(y) * 1j for x, y in lines]

positions = {x + y * 1j for x in range(71) for y in range(71)}
positions -= set(corruptions[:1024])
edges = {pos: {pos + step: 1 for step in [1, 1j, -1, -1j]} for pos in positions}
dist, prev = shortestpaths(edges, [0j])
print(dist[70 + 70j])

# TODO: Binary search for part two
