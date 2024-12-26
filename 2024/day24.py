def toposort(xs):
    deps = {k: v & xs for k, v in all_deps.items() if k in xs}
    while deps:
        no_deps = {x for x, x_deps in deps.items() if not x_deps}
        deps = {x: x_deps - no_deps for x, x_deps in deps.items() if x_deps}
        for x in no_deps:
            yield x

def get_value(gate):
    if gate in values:
        return values[gate]
    elif gate_type[gate] == "AND":
        result = all(get_value(inp) for inp in inputs[gate])
    elif gate_type[gate] == "OR":
        result = any(get_value(inp) for inp in inputs[gate])
    elif gate_type[gate] == "XOR":
        result = sum(get_value(inp) for inp in inputs[gate]) & 1 == 1
    return result

with open("day24.in", "r") as f:
    values, gates = [block.splitlines() for block in f.read().split("\n\n")]
    print("\n".join(sorted(gates)))
    values = {name: int(value) for name, value in (line.split(": ") for line in values)}
    inputs = dict()
    gate_type = dict()
    for gate in gates:
        in1, gate, in2, _, out = gate.split()
        inputs[out] = {in1, in2}
        gate_type[out] = gate
    for gate in gate_type:
        values[gate] = get_value(gate)

binary = 0
for gate, value in sorted(values.items(), reverse=True):
    if gate[0] == "z":
        binary = 2 * binary + value
print(binary)
