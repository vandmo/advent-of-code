from functools import cache
from hashlib import md5
from itertools import count

SALT = "abc"


@cache
def part1_hash(number):
    r = md5(f"{SALT}{number}".encode("ascii")).hexdigest()
    for i in range(len(r) - 2):
        if r[i] == r[i + 1] and r[i] == r[i + 2]:
            return r, r[i]
    return None


@cache
def part2_hash(number):
    r = md5(f"{SALT}{number}".encode()).hexdigest()
    for _ in range(2016):
        r = md5(r.encode()).hexdigest()
    for i in range(len(r) - 2):
        if r[i] == r[i + 1] and r[i] == r[i + 2]:
            return r, r[i]
    return None


def solve(hash_func):
    cnt = 0
    for i in count():
        h = hash_func(i)
        if h is None:
            continue
        h, r = h
        for j in range(i + 1, i + 1001):
            h2 = hash_func(j)
            if h2 is None:
                continue
            h2, _ = h2
            if r * 5 in h2:
                cnt += 1
                if cnt == 64:
                    return i
                break


print("ANSWER PART 1:", solve(part1_hash))
print("ANSWER PART 2:", solve(part2_hash))
