from collections import Counter

input = [line.strip() for line in open("input.txt")]


def is_nice_ridiculous(s):
    counter = Counter(s)
    if sum(counter[vowel] for vowel in "aeiou") < 3:
        return False
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if f"{letter}{letter}" in s:
            break
    else:
        return False
    for bad in ["ab", "cd", "pq", "xy"]:
        if bad in s:
            return False
    return True


assert is_nice_ridiculous("ugknbfddgicrmopn")
assert is_nice_ridiculous("aaa")
assert not is_nice_ridiculous("jchzalrnumimnmhp")
assert not is_nice_ridiculous("haegwjzuvuyypxyu")
assert not is_nice_ridiculous("dvszwmarrgswjxmb")


def is_nice_better(s):
    for i in range(len(s) - 3):
        pair = s[i : i + 2]
        if pair in s[i + 2 :]:
            break
    else:
        return False
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            break
    else:
        return False
    return True


assert is_nice_better("qjhvhtzxzqqjkmpb")
assert is_nice_better("xxyxx")
assert not is_nice_better("uurcxstgmygtbstg")
assert not is_nice_better("ieodomkazucvgmuy")


print(
    "ANSWER PART 1:",
    sum(1 for line in input if is_nice_ridiculous(line)),
)
print(
    "ANSWER PART 2:",
    sum(1 for line in input if is_nice_better(line)),
)
