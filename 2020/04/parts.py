passport = {}
passports = []
for line in open("input.txt"):
    if not line.strip():
        passports.append(passport)
        passport = {}
    entries = line.split()
    for entry in entries:
        k, v = entry.split(":", 1)
        passport[k] = v
passports.append(passport)


def is_valid(passport: dict[str, str]):
    return set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]).issubset(
        passport.keys()
    )


def is_very_valid(passport: dict[str, str]):
    if not is_valid(passport):
        return False
    byr = int(passport["byr"])
    iyr = int(passport["iyr"])
    eyr = int(passport["eyr"])
    hgt = passport["hgt"]
    hcl = passport["hcl"]
    ecl = passport["ecl"]
    pid = passport["pid"]
    if byr < 1920 or byr > 2002:
        return False
    if iyr < 2010 or iyr > 2020:
        return False
    if eyr < 2020 or eyr > 2030:
        return False
    if hgt.endswith("cm"):
        n = int(hgt[:-2])
        if n < 150 or n > 193:
            return False
    elif hgt.endswith("in"):
        n = int(hgt[:-2])
        if n < 59 or n > 76:
            return False
    else:
        return False
    if not hcl.startswith("#") or len(hcl) != 7:
        return False
    if not set(hcl[1:]).issubset(set("0123456789abcdef")):
        return False
    if ecl not in set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
        return False
    if len(pid) != 9 or not set(pid).issubset(set("0123456789")):
        return False
    return True


print("ANSWER PART 1:", sum(1 for passport in passports if is_valid(passport)))
print("ANSWER PART 2:", sum(1 for passport in passports if is_very_valid(passport)))
