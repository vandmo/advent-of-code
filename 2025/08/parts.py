import math

points = []
for line in open("input.txt"):
    point = tuple(int(n) for n in line.split(","))
    points.append(point)

distances = []

for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        p0, p1 = points[i], points[j]
        p0x, p0y, p0z = p0
        p1x, p1y, p1z = p1
        d = (p0x - p1x) ** 2 + (p0y - p1y) ** 2 + (p0z - p1z) ** 2
        distances.append((d, p0, p1))


points_to_component = dict()
components = dict()
for point in points:
    s = points_to_component[point] = set([point])
    components[id(s)] = s


def connect(p0, p1):
    s0 = points_to_component[p0]
    s1 = points_to_component[p1]
    if s0 is s1:
        return
    s = s0 | s1
    for p in s:
        points_to_component[p] = s
    if id(s0) in components:
        del components[id(s0)]
    if id(s1) in components:
        del components[id(s1)]
    components[id(s)] = s


sorted_by_distance = list(sorted(distances))
for _, p0, p1 in sorted_by_distance[0:1000]:
    connect(p0, p1)

part1 = math.prod(
    len(component)
    for component in sorted(components.values(), key=len, reverse=True)[:3]
)

i = 1000
p0 = None
p1 = None
while len(components) > 1:
    _, p0, p1 = sorted_by_distance[i]
    connect(p0, p1)
    i += 1
assert p0 is not None and p1 is not None
part2 = p0[0] * p1[0]

print("ANSWER PART 1:", part1)
print("ANSWER PART 2:", part2)
