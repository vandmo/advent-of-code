from itertools import pairwise, permutations

routes = dict()
destinations = set()

for line in open("input.txt"):
    s, rest = line.split(" to ")
    t, cost = rest.split(" = ")
    cost = int(cost)
    routes[(s, t)] = cost
    routes[(t, s)] = cost
    destinations.add(s)
    destinations.add(t)


def calculate_cost(route):
    return sum(routes[(s, t)] for s, t in pairwise(route))


print(
    "ANSWER PART 1:", min(calculate_cost(route) for route in permutations(destinations))
)
print(
    "ANSWER PART 2:", max(calculate_cost(route) for route in permutations(destinations))
)
