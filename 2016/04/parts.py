from collections import Counter
from dataclasses import dataclass


@dataclass
class Room:
    sector_id: int
    name: str


def get_real_rooms():
    def checksum_for(name):
        counter = Counter(name)
        result = "".join(
            letter for _, letter in sorted((-v, k) for k, v in counter.items())[:5]
        )
        return result

    M = ord("z") - ord("a") + 1

    def decrypt_part(part, sector_id):
        result = ""
        for c in part:
            result += chr(ord("a") + (ord(c) - ord("a") + sector_id) % M)
        return result

    rooms = []
    for line in open("input.txt"):
        parts = line.strip().split("-")
        name_parts = parts[:-1]
        name = "".join(name_parts)
        rest = parts[-1]
        sector_id, checksum = rest.split("[")
        sector_id = int(sector_id)
        checksum = checksum[:-1]
        if checksum == checksum_for(name):
            rooms.append(
                Room(
                    sector_id=sector_id,
                    name=" ".join(decrypt_part(part, sector_id) for part in name_parts),
                )
            )

    return rooms


rooms = get_real_rooms()

print("ANSWER PART 1:", sum(room.sector_id for room in rooms))
for room in rooms:
    if room.name == "northpole object storage":
        print("ANSWER PART 2:", room.sector_id)
        break
else:
    for room in rooms:
        print(room)
    print("^^^ Find it there ^^^")
