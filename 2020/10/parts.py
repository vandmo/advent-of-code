from functools import cache
from itertools import pairwise

ADAPTERS = [int(line) for line in open("input.txt")]
ADAPTERS.sort()

j1 = 0
j3 = 1  # 3 jolts to target adapter
for a, b in pairwise([0] + ADAPTERS):
    match b - a:
        case 1:
            j1 += 1
        case 3:
            j3 += 1
        case _:
            assert False

print("ANSWER PART 1:", j1 * j3)

TARGET = max(ADAPTERS) + 3


@cache
def ways_to_make(at: int, adapters: tuple[int, ...]):
    n = 0 if TARGET - at > 3 else 1
    for i in range(len(adapters)):
        candidate = adapters[i]
        if candidate - at > 3:
            break
        if candidate < at:
            continue
        n += ways_to_make(candidate, adapters[i + 1 :])
    return n


print("ANSWER PART 2:", ways_to_make(0, tuple(ADAPTERS)))
