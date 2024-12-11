from functools import cache

line = "125 17"

nums = [int(n) for n in line.split(" ")]


def blink(stones):
    new = []
    for stone in stones:
        if stone == 0:
            new.append(1)
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            new.append(int(s[0 : len(s) // 2]))
            new.append(int(s[len(s) // 2 :]))
        else:
            new.append(stone * 2024)
    return new


@cache
def count_after(n, left):
    assert left >= 0
    if left == 0:
        return 1
    elif n == 0:
        return count_after(1, left - 1)
    elif len(str(n)) % 2 == 0:
        s = str(n)
        I = int(s[0 : len(s) // 2])
        J = int(s[len(s) // 2 :])
        return count_after(I, left - 1) + count_after(J, left - 1)
    else:
        return count_after(n * 2024, left - 1)


print("ANSWER PART1", sum(count_after(n, 25) for n in nums))
print("ANSWER PART2", sum(count_after(n, 75) for n in nums))
