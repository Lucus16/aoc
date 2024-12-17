with open("day17.in", "r") as f:
    _, _, a, _, _, b, _, _, c, _, program = f.read().split()
    a, b, c = int(a), int(b), int(c)
    program = [int(x) for x in program.split(",")]

def run(a, b, c, ip=0):
    while ip + 1 < len(program):
        opcode = program[ip]
        literal = program[ip + 1]
        combo = [0, 1, 2, 3, a, b, c, None][literal]
        ip += 2
        if opcode == 0:
            a >>= combo
        elif opcode == 1:
            b ^= literal
        elif opcode == 2:
            b = combo & 7
        elif opcode == 3 and a:
            ip = literal
        elif opcode == 4:
            b ^= c
        elif opcode == 5:
            yield combo & 7
        elif opcode == 6:
            b = a >> combo
        elif opcode == 7:
            c = a >> combo

print(",".join(str(x) for x in run(a, b, c)))
options = {0}
for i in reversed(range(len(program))):
    options = {
        a
        for option in options
        for a in range(option * 8, option * 8 + 8)
        if list(run(a, b, c)) == program[i:]
    }
print(min(options))
