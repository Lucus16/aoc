numpad = ["789", "456", "123", " 0A"]
numpad = {cell: (x, y) for y, row in enumerate(numpad) for x, cell in enumerate(row) if cell != " "}
dirpad = [" ^A", "<v>"]
dirpad = {cell: (x, y) for y, row in enumerate(dirpad) for x, cell in enumerate(row) if cell != " "}

def routes(src, dst, pad):
    sx, sy = pad[src]
    dx, dy = pad[dst]
    if (dx, sy) in pad.values():
        yield ">" * (dx - sx) + "<" * (sx - dx) + "^" * (sy - dy) + "v" * (dy - sy) + "A"
    if (sx, dy) in pad.values():
        yield "^" * (sy - dy) + "v" * (dy - sy) + ">" * (dx - sx) + "<" * (sx - dx) + "A"

def cost(code, costs):
    return sum(costs[x][y] for x, y in zip("A" + code, code))

def indirect_costs(costs, pad):
    return {
        src: {
            dst: min(cost(route, costs) for route in routes(src, dst, pad))
            for dst in pad
        }
        for src in pad
    }

def complexity(code, indirections):
    costs = {x: {y: 1 for y in dirpad} for x in dirpad}
    for indirection in range(indirections):
        costs = indirect_costs(costs, dirpad)
    costs = indirect_costs(costs, numpad)
    return cost(code, costs) * int(code[:-1])

with open("day21.in", "r") as f:
    codes = f.read().splitlines()

print(sum(complexity(code, 2) for code in codes))
print(sum(complexity(code, 25) for code in codes))
