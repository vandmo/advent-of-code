banks = tuple(int(n) for n in open("input.txt").read().strip().split())

seen = {}


def redist(banks):
    new = list(banks)
    m = max(new)
    i = new.index(m)
    new[i] = 0
    for _ in range(m):
        i = (i + 1) % len(new)
        new[i] += 1
    return tuple(new)


p2 = None
count = 0
while True:
    if banks in seen:
        p2 = seen[banks]
        break
    seen[banks] = count
    banks = redist(banks)
    count += 1
print("ANSWER PART 1:", count)
print("ANSWER PART 2:", count - p2)
