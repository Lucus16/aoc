from collections import defaultdict

with open("day5.in", "r") as f:
    rules, updates = f.read().split("\n\n")

rules = (rule.split("|") for rule in rules.splitlines())
updates = [list(update.split(",")) for update in updates.splitlines()]
all_deps = defaultdict(set)
for before, after in rules:
    all_deps[after].add(before)

def toposort(xs):
    deps = {k: v & xs for k, v in all_deps.items() if k in xs}
    while deps:
        no_deps = {x for x, x_deps in deps.items() if not x_deps}
        deps = {x: x_deps - no_deps for x, x_deps in deps.items() if x_deps}
        for x in no_deps:
            yield x

print(sum(int(u[len(u) // 2]) for u in updates if list(toposort(set(u))) == u))
bad_updates = [set(u) for u in updates if list(toposort(set(u))) != u]
fixed_updates = [list(toposort(u)) for u in bad_updates]
print(sum(int(u[len(u) // 2]) for u in fixed_updates))
