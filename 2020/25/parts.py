from itertools import count

card_pub, door_pub = [int(line.strip()) for line in open("input.txt")]


def find_loop_size(pub_key):
    s = 7
    for i in count(1):
        if s == pub_key:
            return i
        s = (s * 7) % 20201227


def transform(subject_number, loop_size):
    s = subject_number
    for _ in range(loop_size - 1):
        s = (s * subject_number) % 20201227
    return s


card_loop_size = find_loop_size(card_pub)
door_loop_size = find_loop_size(door_pub)

key1 = transform(card_pub, door_loop_size)
key2 = transform(door_pub, card_loop_size)
assert key1 == key2
print("ANSWER PART 1:", key1)
