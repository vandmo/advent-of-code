from itertools import pairwise, permutations

nc = dict()
people = set()
for line in open("input.txt"):
    left, right = line.split(" happiness units by sitting next to ")
    neighbour, _ = right.split(".")
    if "gain" in left:
        person, cost = left.split(" would gain ")
        cost = int(cost)
    else:
        person, cost = left.split(" would lose ")
        cost = -int(cost)
    people.add(person)
    nc[person, neighbour] = cost


def calculate_cost(arr):
    cost = 0
    for a, b in pairwise(arr + (arr[0],)):
        cost += nc.get((a, b), 0) + nc.get((b, a), 0)
    return cost


print("ANSWER PART 1:", max(calculate_cost(arr) for arr in permutations(people)))
people.add("Vandmo")
print("ANSWER PART 2:", max(calculate_cost(arr) for arr in permutations(people)))
