with open("day1.in", "r") as f:
    xys = [line.split() for line in f]
    xs = sorted(int(xy[0]) for xy in xys)
    ys = sorted(int(xy[1]) for xy in xys)

print(sum(abs(x - y) for x, y in zip(xs, ys)))
print(sum(x * ys.count(x) for x in xs))
