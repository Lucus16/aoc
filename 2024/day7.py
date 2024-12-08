with open("day7.in", "r") as f:
    lines = (line.split(": ") for line in f)
    equations = [(int(result), [int(v) for v in vs.split()]) for result, vs in lines]

def options(values, include_concat):
    y = values[-1]
    if len(values) == 1:
        yield y
    else:
        for x in options(values[:-1], include_concat):
            yield x + y
            yield x * y
            if include_concat:
                yield int(str(x) + str(y))

print(sum(result for result, values in equations if result in options(values, False)))
print(sum(result for result, values in equations if result in options(values, True)))
