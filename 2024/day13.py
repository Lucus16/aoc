import re

class Machine:
    def __init__(self, block):
        ax, ay, bx, by, px, py = [int(x) for x in re.findall(r"\d+", block)]
        self.da = ax + ay * 1j
        self.db = bx + by * 1j
        self.prize = px + py * 1j

    def win(self):
        # Rotate the coordinates so one button has no Y coordinate and the remaining Y coordinates
        # describe the number of presses of the other button only.
        a = round((self.prize / self.db).imag / (self.da / self.db).imag)
        b = round((self.prize / self.da).imag / (self.db / self.da).imag)
        return 3 * a + b if a * self.da + b * self.db == self.prize else 0

with open("day13.in", "r") as f:
    machines = [Machine(block) for block in f.read().split("\n\n")]

print(sum(machine.win() for machine in machines))
for machine in machines:
    machine.prize += 10000000000000 + 10000000000000j
print(sum(machine.win() for machine in machines))
