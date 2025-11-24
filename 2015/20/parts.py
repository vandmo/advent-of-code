from itertools import count

INPUT = 130
FASTIFIER = 10


def part1():
    print("--- PART 1")
    A = [10] * INPUT

    print("Speed should increase...")
    for i in range(2, INPUT):
        if i % 1000 == 0:
            print("Progress", i)
        house = i
        while house < INPUT // FASTIFIER:
            A[house] += i * 10
            house += i
        if A[i] >= INPUT:
            return i
    else:
        raise Exception("Answer not found! Try lowering the FASTIFIER...")


def part2():
    print("--- PART 2")
    a = dict()

    for i in count(1):
        if i % 10_000 == 0:
            print("Progress", i)
        house = i
        for _ in range(50):
            p = a.get(house, 0)
            p += i * 11
            a[house] = p
            house += i
        if a[i] >= INPUT:
            return i


p1 = part1()
p2 = part2()
print("--- DONE")
print("ANSWER PART 1:", p1)
print("ANSWER PART 2:", p2)
