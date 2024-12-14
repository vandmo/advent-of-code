from collections import defaultdict
from dataclasses import dataclass

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

W = 101
H = 103


@dataclass(unsafe_hash=True)
class P:
    x: int
    y: int

    def __add__(self, other):
        return P(self.x + other.x, self.y + other.y)


@dataclass
class Robot:
    p: P
    v: P


robots = []
for line in lines:
    p, v = line.split(" ")
    px, py = p.split(",")
    vx, vy = v.split(",")
    robots.append(
        Robot(P(int(px.split("=")[1]), int(py)), P(int(vx.split("=")[1]), int(vy)))
    )


def tick():
    for robot in robots:
        robot.p = robot.p + robot.v
        if robot.p.x < 0:
            robot.p.x = W + robot.p.x
        if robot.p.y < 0:
            robot.p.y = H + robot.p.y
        if robot.p.x >= W:
            robot.p.x = robot.p.x % W
        if robot.p.y >= H:
            robot.p.y = robot.p.y % H


seconds = 0
while True:
    grid = defaultdict(lambda: ".")
    for robot in robots:
        grid[robot.p] = "#"
    lines = []
    for y in range(H):
        line = ""
        for x in range(W):
            line += grid[P(x, y)]
        if "###############################" in line:
            print("ANSWER", seconds)
            break
        lines.append(line)
    else:
        seconds += 1
        tick()
        continue
    break
