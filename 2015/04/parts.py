from hashlib import md5
from itertools import count

IN = "abcdef"


def search(prefix):
    for i in count(1):
        m = md5()
        m.update(f"{IN}{i}".encode("utf-8"))
        if m.hexdigest().startswith(prefix):
            return i


print("ANSWER PART 1:", search("00000"))
print("ANSWER PART 2:", search("000000"))
