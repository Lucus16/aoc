width, height = 101, 103

class Robot:
    def __init__(self, line):
        import re
        self.x, self.y, self.dx, self.dy = [int(n) for n in re.findall(r"-?\d+", line)]

    def locate(self, seconds):
        return ((self.x + self.dx * seconds) % width, (self.y + self.dy * seconds) % height)

with open("day14.in", "r") as f:
    robots = [Robot(line) for line in f]

positions = [robot.locate(100) for robot in robots]
q1 = sum(1 for x, y in positions if x < width // 2 and y < height // 2)
q2 = sum(1 for x, y in positions if x > width // 2 and y < height // 2)
q3 = sum(1 for x, y in positions if x < width // 2 and y > height // 2)
q4 = sum(1 for x, y in positions if x > width // 2 and y > height // 2)
print(q1 * q2 * q3 * q4)

def rate(positions):
    # Score is number of positions with horizontal neighbors
    return sum(1 for x, y in positions if (x - 1, y) in positions)

rating, dt = max((rate({robot.locate(dt) for robot in robots}), dt) for dt in range(width * height))
positions = {robot.locate(dt) for robot in robots}
for y in range(height):
    print("".join("*" if (x, y) in positions else " " for x in range(width)))
print(dt)
