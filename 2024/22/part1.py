with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]


def calculate(n):
    for _ in range(2000):
        n = ((64 * n) ^ n) % 16777216
        n = ((n // 32) ^ n) % 16777216
        n = ((n * 2048) ^ n) % 16777216
    return n


print("ANSWER", sum(calculate(int(line)) for line in lines))
