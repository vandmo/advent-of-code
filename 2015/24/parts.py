from functools import reduce
from itertools import combinations
from operator import mul

weights = sorted(int(x) for x in open("input.txt"))


def part1():
    for i in range(len(weights)):
        for g1 in combinations(weights, i):
            rest = set(weights) - set(g1)
            if sum(g1) * 2 == sum(rest):
                for j in range(len(rest)):
                    for g2 in combinations(rest, j):
                        if sum(g2) == sum(rest - set(g2)):
                            return g1
    assert False


def part2():
    for i in range(len(weights)):
        for g1 in combinations(weights, i):
            rest = set(weights) - set(g1)
            S = sum(g1)
            if S * 3 == sum(rest):
                for j in range(len(rest)):
                    for g2 in combinations(rest, j):
                        rest2 = rest - set(g2)
                        if sum(g2) == S and sum(rest2) == S * 2:
                            for k in range(len(rest2)):
                                for g3 in combinations(rest2, k):
                                    if sum(g3) == S and sum(rest2 - set(g3)) == S:
                                        return g1
    assert False


print("ANSWER PART 1:", reduce(mul, part1(), 1))
print("ANSWER PART 2:", reduce(mul, part2(), 1))
