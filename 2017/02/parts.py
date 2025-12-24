from itertools import combinations


def calc1(nums):
    return max(nums) - min(nums)


def calc2(nums):
    for a, b in combinations(nums, 2):
        if a % b == 0 or b % a == 0:
            return max(a, b) // min(a, b)
    assert False


lines = [line.strip() for line in open("input.txt")]
print("ANSWER PART 1:", sum(calc1([int(n) for n in line.split()]) for line in lines))
print("ANSWER PART 2:", sum(calc2([int(n) for n in line.split()]) for line in lines))
