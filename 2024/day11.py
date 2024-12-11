from functools import cache

with open("day11.in", "r") as f:
    stones = [int(x) for x in f.read().split()]

def step(stone):
    s = str(stone)
    if stone == 0:
        yield 1
    elif len(s) % 2 == 0:
        yield int(s[:len(s) // 2])
        yield int(s[len(s) // 2:])
    else:
        yield 2024 * stone

@cache
def count(stone, blinks):
    return 1 if blinks <= 0 else sum(count(s, blinks - 1) for s in step(stone))

print(sum(count(s, 25) for s in stones))
print(sum(count(s, 75) for s in stones))
