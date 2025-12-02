lines = [line.strip() for line in open("input.txt")]


def parse(ip: str):
    class ParsedIp:
        def __init__(self):
            self.supernets = []
            self.hypernets = []

    r = ParsedIp()
    while True:
        splitted = ip.split("[", maxsplit=1)
        if len(splitted) == 1:
            if splitted[0]:
                r.supernets.append(splitted[0])
            break
        a, ip = splitted
        b, ip = ip.split("]", maxsplit=1)
        if a:
            r.supernets.append(a)
        if b:
            r.hypernets.append(b)
    return r


def supports_tls(ip: str):
    def has_abba(part):
        for i in range(len(part) - 3):
            if (
                part[i] != part[i + 1]
                and part[i] == part[i + 3]
                and part[i + 1] == part[i + 2]
            ):
                return True
        return False

    parsed = parse(ip)
    if any(has_abba(hypernet) for hypernet in parsed.hypernets):
        return False
    return any(has_abba(supernet) for supernet in parsed.supernets)


def supports_ssl(ip: str):
    parsed = parse(ip)
    babs = set()
    for supernet in parsed.supernets:
        for i in range(len(supernet) - 2):
            if supernet[i] == supernet[i + 2] and supernet[i] != supernet[i + 1]:
                babs.add(f"{supernet[i+1]}{supernet[i]}{supernet[i+1]}")
    for bab in babs:
        for hypernet in parsed.hypernets:
            if bab in hypernet:
                return True
    return False


assert supports_tls("abba[mnop]qrst")
assert not supports_tls("abcd[bddb]xyyx")
assert not supports_tls("aaaa[qwer]tyui")
assert supports_tls("ioxxoj[asdfgh]zxcvbn")

assert supports_ssl("aba[bab]xyz")
assert not supports_ssl("xyx[xyx]xyx")
assert supports_ssl("aaa[kek]eke")
assert supports_ssl("zazbz[bzb]cdb")

print("ANSWER PART 1:", sum(1 for line in lines if supports_tls(line)))
print("ANSWER PART 2:", sum(1 for line in lines if supports_ssl(line)))
