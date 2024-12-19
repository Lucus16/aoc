from functools import cache

with open("day19.in", "r") as f:
    towels, patterns = f.read().split("\n\n")
    towels = towels.split(", ")

@cache
def count(pat):
    return sum(count(pat[:-len(towel)]) for towel in towels if pat.endswith(towel)) if pat else 1

counts = [count(pattern) for pattern in patterns.splitlines() if count(pattern)]
print(len(counts), sum(counts), sep="\n")
