with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

L = sorted([int(l.split("   ")[0]) for l in lines])
R = sorted([int(l.split("   ")[1]) for l in lines])
S = 0
for i in range(len(L)):
    S += abs(L[i] - R[i])

print("ANSWER", S)
