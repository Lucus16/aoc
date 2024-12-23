from collections import defaultdict, Counter

with open("day23.in", "r") as f:
    computers = defaultdict(set)
    for line in f:
        a, b = line.strip().split("-")
        computers[a].add(b)
        computers[b].add(a)

triangles = {
    frozenset([a, b, c])
    for a in computers
    for b in computers[a]
    for c in computers[a] & computers[b]
}

print(sum(1 for tri in triangles if any(name[0] == "t" for name in tri)))

def max_clique(graph):
    best = set()
    while graph:
        x, ax = next(iter(graph.items()))
        max_x_clique = {x} | max_clique({y: ay & ax for y, ay in graph.items() if y in ax})
        if len(max_x_clique) > len(best):
            best = max_x_clique
        graph = {y: ay - {x} for y, ay in graph.items() if y != x}
    return best

print(",".join(sorted(max_clique(computers))))
