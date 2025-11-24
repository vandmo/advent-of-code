from math import prod

monster = (
    """
|                  # 
|#    ##    ##    ###
| #  #  #  #  #  #
""".strip()
    .replace("|", "")
    .splitlines()
)

monster_coords = []
for y, line in enumerate(monster):
    monster_coords.extend([(x, y) for x, c in enumerate(line) if c == "#"])


class Tile:
    def __init__(self, id: int, lines: list[str]) -> None:
        self.id = id
        self._lines = lines
        self._wh = len(lines[0])
        assert self._wh == len(lines)

    def lefts(self):
        left = "".join(line[0] for line in self._lines)
        return left, left[::-1]

    def rights(self):
        right = "".join(line[-1] for line in self._lines)
        return right, right[::-1]

    def ups(self):
        return self._lines[0], self._lines[0][::-1]

    def downs(self):
        return self._lines[-1], self._lines[-1][::-1]

    def sides(self):
        return self.downs() + self.ups() + self.lefts() + self.rights()

    def rotate90cw(self):
        lines = []
        for i in range(self._wh):
            lines.append("".join(line[i] for line in reversed(self._lines)))
        self._lines = lines

    def flip(self):
        for i in range(self._wh):
            self._lines[i] = self._lines[i][::-1]

    def mutate_until(self, check):
        if check():
            return
        self.rotate90cw()
        if check():
            return
        self.rotate90cw()
        if check():
            return
        self.rotate90cw()
        if check():
            return
        self.flip()
        if check():
            return
        self.rotate90cw()
        if check():
            return
        self.rotate90cw()
        if check():
            return
        self.rotate90cw()
        if check():
            return
        assert False

    def make_left(self, side):
        self.mutate_until(lambda: self.lefts()[0] == side)

    def make_up(self, side):
        self.mutate_until(lambda: self.ups()[0] == side)

    def strip_borders(self):
        self._lines = [line[1:-1] for line in self._lines[1:-1]]

    def _to_grid(self):
        grid = dict()
        for y, line in enumerate(self._lines):
            for x, c in enumerate(line):
                grid[x, y] = c
        return grid

    def _monster_origins(self):
        grid = self._to_grid()
        monster_origins = []
        for x in range(self._wh):
            for y in range(self._wh):
                for mx, my in monster_coords:
                    if grid.get((x + mx, y + my), ".") != "#":
                        break
                else:
                    monster_origins.append((x, y))
        return monster_origins

    def count_monsters(self):
        return len(self._monster_origins())

    def nullify_monsters(self):
        grid = self._to_grid()
        for x, y in self._monster_origins():
            for mx, my in monster_coords:
                grid[x + mx, y + my] = "O"
        for y in range(self._wh):
            line = ""
            for x in range(self._wh):
                line += grid[x, y]
            print(line)
        return sum(1 for c in grid.values() if c == "#")


def parse():
    tiles: dict[int, Tile] = dict()
    tile_id: int | None = None
    lines: list[str] | None = None
    for line in open("input.txt"):
        line = line.strip()
        if not line:
            continue
        if line.startswith("Tile "):
            if tile_id is not None:
                assert lines is not None
                tiles[tile_id] = Tile(tile_id, lines)
            _, p2, *_ = line.split()
            tile_id = int(p2.removesuffix(":"))
            lines = []
        else:
            assert lines is not None
            lines.append(line.strip())
    assert lines is not None and tile_id is not None
    tiles[tile_id] = Tile(tile_id, lines)
    return tiles


tiles: dict[int, Tile] = parse()

side_to_tile_id: dict[str, list[int]] = dict()

for tile_id, tile in tiles.items():
    for side in tile.sides():
        side_to_tile_id.setdefault(side, []).append(tile_id)


def find_corners():
    neibour_count = dict()
    for v in side_to_tile_id.values():
        assert v
        C = len(v) - 1
        if C > 0:
            for tile in v:
                neibour_count[tile] = neibour_count.get(tile, 0) + C

    return [tile_id for tile_id, nc in neibour_count.items() if nc == 4]


corners = find_corners()
assert len(corners) == 4

corner = tiles[corners[0]]


def find_neighbour(tile: Tile, side: tuple[str, str]):
    ns = set(side_to_tile_id[side[0]] + side_to_tile_id[side[1]])
    ns.remove(tile.id)
    if ns:
        assert len(ns) == 1
        return ns.pop()
    return None


# Rotate a corner so it represents the upper right corner
rn = find_neighbour(corner, corner.rights())
ln = find_neighbour(corner, corner.lefts())
un = find_neighbour(corner, corner.ups())
dn = find_neighbour(corner, corner.downs())
match rn, ln, un, dn:
    case None, int(), None, int():
        corner.rotate90cw()
        corner.rotate90cw()
        corner.rotate90cw()
    case None, int(), int(), None:
        corner.rotate90cw()
        corner.rotate90cw()
    case int(), int(), None, None:
        corner.rotate90cw()
        corner.rotate90cw()
    case int(), None, None, int():
        pass
    case _:
        assert False


def make_tile_lines(corner):
    down_tile = corner
    tile_lines: list[list[Tile]] = []
    while True:
        right_tile = down_tile
        tile_lines.append([])
        while True:
            tile_lines[-1].append(right_tile)
            prev_rights = right_tile.rights()
            rn_id = find_neighbour(right_tile, prev_rights)
            if rn_id is None:
                break
            right_tile = tiles[rn_id]
            right_tile.make_left(prev_rights[0])
        prev_downs = down_tile.downs()
        dn_id = find_neighbour(down_tile, prev_downs)
        if dn_id is None:
            break
        down_tile = tiles[dn_id]
        down_tile.make_up(prev_downs[0])
    return tile_lines


tile_lines = make_tile_lines(corner)
part1 = prod(tile_lines[x][y].id for x in range(-1, 1) for y in range(-1, 1))

for tile in tiles.values():
    tile.strip_borders()


def make_mega_tile(tile_lines):
    mega_tiles_lines = []
    for tile_line in tile_lines:
        for i in range(len(tile_line[0]._lines)):
            line = ""
            for tile in tile_line:
                line += tile._lines[i]
            mega_tiles_lines.append(line)

    return Tile(0, mega_tiles_lines)


mega_tile = make_mega_tile(tile_lines)

mega_tile.mutate_until(lambda: mega_tile.count_monsters() > 0)
number_of_monsters = mega_tile.count_monsters()
part2 = mega_tile.nullify_monsters()
print("Corners:", corners)
print("Number of monsters:", number_of_monsters)
print("ANSWER PART 1:", part1)
print("ANSWER PART 2:", part2)
