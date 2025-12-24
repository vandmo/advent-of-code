S = open("input.txt").read().strip()
print(
    "ANSWER PART 1:",
    sum(
        int(a)
        for a, b in ((S[i], S[(i + 1) % len(S)]) for i in range(len(S)))
        if a == b
    ),
)
print(
    "ANSWER PART 2:",
    sum(
        int(a)
        for a, b in ((S[i], S[(i + len(S) // 2) % len(S)]) for i in range(len(S)))
        if a == b
    ),
)
