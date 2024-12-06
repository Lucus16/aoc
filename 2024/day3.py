import re

with open("day3.in", "r") as f:
    memory = f.read()

def mul_sum(memory):
    muls = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", memory)
    return sum(int(mul[0]) * int(mul[1]) for mul in muls)

print(mul_sum(memory))
print(mul_sum(re.sub(r"don't\(\).*?(do\(\)|$)", "#", memory, flags=re.DOTALL)))
