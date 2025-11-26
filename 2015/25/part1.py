def pos(*, row, column):
    n = row + column - 2
    before = (n * (n + 1)) // 2
    return before + column


left, right = open("input.txt").read().strip().split(" row ")
row, column = right.split(", column ")
P = pos(row=int(row), column=int(column.removesuffix(".")))
M = 33554393
print("ANSWER PART 1:", (20151125 * pow(252533, P - 1, M)) % M)
