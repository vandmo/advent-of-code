import heapq
import math
from collections import defaultdict


def dijkstra_shortest_path(edges, source, target=None, *, all_paths: bool = False):
    """edges is a collection of tuples with (source, edge, distance)"""
    distances = defaultdict(lambda: math.inf)
    source_to_edges = defaultdict(list)
    for edge in edges:
        source_to_edges[edge[0]].append(edge)
    prev = dict()
    visited = set()
    distances[source] = 0
    priority_queue = [(0, source)]
    while priority_queue:
        _, u = heapq.heappop(priority_queue)
        if u == target:
            return distances, prev
        visited.add(u)
        for _, v, distance_to_v in source_to_edges[u]:
            if v in visited:
                continue
            alt = distances[u] + distance_to_v
            if all_paths:
                if alt <= distances[v]:
                    distances[v] = alt
                    if not v in prev:
                        prev[v] = (u,)
                    else:
                        prev[v] += (u,)
                    heapq.heappush(priority_queue, (alt, v))
            else:
                if alt < distances[v]:
                    distances[v] = alt
                    prev[v] = u
                    heapq.heappush(priority_queue, (alt, v))
    return distances, prev
