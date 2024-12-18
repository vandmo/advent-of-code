from algorithms import dijkstra_shortest_path
from vector2d import *

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

START = ORIGIN
END = Vector2D(70, 70)
bounds = InclusiveBounds2D(START, END)

corrupted = set(Vector2D(*(int(n) for n in lines[i].split(","))) for i in range(1024))

edges = set()
for v in bounds.discrete_points():
    if v in corrupted:
        continue
    for direction in (UP, DOWN, LEFT, RIGHT):
        neigbour = v + direction
        if neigbour in bounds and neigbour not in corrupted:
            edges.add((v, neigbour, 1))
distances, paths = dijkstra_shortest_path(edges, START, END)

print("ANSWER", distances[END])
