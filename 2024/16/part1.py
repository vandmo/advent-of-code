from algorithms import dijkstra_shortest_path
from vector2d import *

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

grid = dict()
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        p = Vector2D(x, y)
        if c == "S":
            start = p
            grid[p] = "."
        elif c == "E":
            end = p
            grid[p] = "."
        else:
            grid[p] = c

W = len(lines[0])
H = len(lines)

edges = set()
for x in range(W):
    for y in range(H):
        p = Vector2D(x, y)
        if grid[p] != ".":
            continue
        if grid[p + EAST] == ".":
            T = (p + EAST, "E")
            edges.add(((p, "E"), T, 1))
            edges.add(((p, "N"), T, 1001))
            edges.add(((p, "S"), T, 1001))
        if grid[p + WEST] == ".":
            T = (p + WEST, "W")
            edges.add(((p, "W"), T, 1))
            edges.add(((p, "N"), T, 1001))
            edges.add(((p, "S"), T, 1001))
        if grid[p + NORTH] == ".":
            T = (p + NORTH, "N")
            edges.add(((p, "N"), T, 1))
            edges.add(((p, "E"), T, 1001))
            edges.add(((p, "W"), T, 1001))
        if grid[p + SOUTH] == ".":
            T = (p + SOUTH, "S")
            edges.add(((p, "S"), T, 1))
            edges.add(((p, "E"), T, 1001))
            edges.add(((p, "W"), T, 1001))

distances, paths = dijkstra_shortest_path(edges, (start, "E"), (end, "N"))

print("ANSWER", min(distances[(end, "N")] for D in "NSEW"))
