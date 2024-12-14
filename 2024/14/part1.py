from dataclasses import dataclass

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

W = 101
H = 103


@dataclass
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


for _ in range(100):
    tick()

q0 = 0
q1 = 0
q2 = 0
q3 = 0

for robot in robots:
    if robot.p.x < W // 2 and robot.p.y < H // 2:
        q0 += 1
    elif robot.p.x > W // 2 and robot.p.y < H // 2:
        q1 += 1
    elif robot.p.x > W // 2 and robot.p.y > H // 2:
        q2 += 1
    elif robot.p.x < W // 2 and robot.p.y > H // 2:
        q3 += 1
print("ANSWER", q0 * q1 * q2 * q3)
