INPUT = "111221"


def apply(digits):
    r = ""
    prev = digits[0]
    count = 1
    for d in digits[1:] + "E":
        if d == prev:
            count += 1
        else:
            r += f"{count}{prev}"
            count = 1
            prev = d
    return r


assert apply("111221") == "312211"

answer = INPUT
for _ in range(40):
    answer = apply(answer)
print("ANSWER PART 1:", len(answer))
for _ in range(10):
    answer = apply(answer)
print("ANSWER PART 2:", len(answer))
