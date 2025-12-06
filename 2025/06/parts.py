from math import prod


lines = [line.strip("\n") for line in open("input.txt") if line.strip()]


def part1():
    operators = lines[-1].split()
    numbers = [[int(n) for n in line.split()] for line in lines[:-1]]

    def count_column(column_idx):
        match operators[column_idx]:
            case "+":
                return sum(column[column_idx] for column in numbers)
            case "*":
                return prod(column[column_idx] for column in numbers)
            case _:
                assert False

    return sum(count_column(column_idx) for column_idx in range(len(numbers[0])))


def part2():
    problems = [[]]
    for column_idx in range(len(lines[0]) - 1, -1, -1):
        column = ""
        for line in lines:
            column += line[column_idx]
        if not column.strip():
            problems.append([])
        else:
            problems[-1].append(column)

    def solve(problem):
        op = problem[-1][-1]
        problem[-1] = problem[-1][:-1]
        match op:
            case "+":
                return sum(int(n) for n in problem)
            case "*":
                return prod(int(n) for n in problem)
            case _:
                assert False
        return 1

    return sum(solve(problem) for problem in problems)


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
