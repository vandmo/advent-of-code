INPUT = "0,3,6"

starting_numbers = [int(x) for x in INPUT.split(",")]


def solve(N):
    previous_positions = dict()

    for pos, num in enumerate(starting_numbers):
        previous_positions[num] = [pos]

    v = starting_numbers[-1]
    for i in range(N - len(starting_numbers)):
        prevs = previous_positions.get(v, [])
        if len(prevs) > 1:
            n = prevs[-1] - prevs[-2]
            previous_positions.setdefault(n, []).append(prevs[-1] + 1)
            v = n
        else:
            previous_positions.setdefault(0, []).append(prevs[-1] + 1)
            v = 0
    return v


print("ANSWER PART 1:", solve(2020))
print("ANSWER PART 2:", solve(30000000))
