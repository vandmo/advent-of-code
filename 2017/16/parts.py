I = [*"abcdefghijklmnop"]


def spin(amount):
    global I
    break_at = amount % len(I)
    I = I[-break_at:] + I[:-break_at]


def swap_at(i0, i1):
    v = I[i0]
    I[i0] = I[i1]
    I[i1] = v


def swap(p0, p1):
    swap_at(I.index(p0), I.index(p1))


MOVES = open("input.txt").read().strip().split(",")

arrangements = []
while True:
    if "".join(I) in arrangements:
        break
    else:
        arrangements.append("".join(I))
    for dance_move in MOVES:
        match dance_move[0]:
            case "s":
                spin(int(dance_move[1:]))
            case "x":
                l, r = [int(n) for n in dance_move[1:].split("/")]
                swap_at(l, r)
            case "p":
                l, r = dance_move[1:].split("/")
                swap(l, r)

print("ANSWER PART 1:", arrangements[1])
print("ANSWER PART 2:", arrangements[1000000000 % len(arrangements)])
