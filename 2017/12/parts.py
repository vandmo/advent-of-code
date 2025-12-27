pipes = {}

for line in open("input.txt"):
    line = line.strip()
    L, R = line.split(" <-> ")
    for target in R.split(", "):
        pipes.setdefault(L, set()).add(target)
        pipes.setdefault(target, set()).add(L)


def part1():
    visited = set()

    def visit(n):
        if n in visited:
            return
        visited.add(n)
        for t in pipes[n]:
            visit(t)

    visit("0")
    return len(visited)


def part2():
    all_programs = set(pipes.keys())
    cnt = 0
    while all_programs:
        cnt += 1
        visited = set()

        def visit(n):
            if n in visited:
                return
            visited.add(n)
            for t in pipes[n]:
                visit(t)

        visit(all_programs.pop())
        all_programs = all_programs - visited
    return cnt


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
