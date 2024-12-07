with open("input.txt") as f:
    line = f.read()

s = 0
c = 0


def readC():
    global c
    if c < len(line):
        R = line[c]
        c += 1
        return R
    return None


C = readC()
state = "start"
lnum = ""
rnum = ""


def reset():
    global state
    global lnum
    global rnum
    global c
    state = "start"
    lnum = ""
    rnum = ""


while C != None:
    if state == "start":
        if C == "m":
            state = "expect_u"
        else:
            reset()
    elif state == "expect_u":
        if C == "u":
            state = "expect_l"
        else:
            reset()
    elif state == "expect_l":
        if C == "l":
            state = "expect_lparen"
        else:
            reset()
    elif state == "expect_lparen":
        if C == "(":
            state = "expect_lnum"
        else:
            reset()
    elif state == "expect_lnum":
        if C in "0123456789":
            lnum += C
        elif C == ",":
            state = "expect_rnum"
        else:
            reset()
    elif state == "expect_rnum":
        if C in "0123456789":
            rnum += C
        elif C == ")":
            s += int(lnum) * int(rnum)
            reset()
        else:
            reset()
    else:
        reset()
    C = readC()

print("ANSWER", s)
