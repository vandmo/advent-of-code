from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Vector2D:
    x: int | float
    y: int | float

    def __post_init__(self):
        if not isinstance(self.x, int) and not isinstance(self.x, float):
            raise TypeError(f"expected x to be an int or a float")
        if not isinstance(self.y, int) and not isinstance(self.y, float):
            raise TypeError(f"expected y to be an int or a float")

    def __iter__(self):
        return iter((self.x, self.y))

    def __add__(self, other):
        if isinstance(other, tuple):
            return Vector2D(self.x + other[0], self.y + other[1])
        elif isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, tuple):
            return Vector2D(self.x + other[0], self.y + other[1])
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, tuple):
            return Vector2D(self.x - other[0], self.y - other[1])
        elif isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        else:
            return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, tuple):
            return Vector2D(self.x - other[0], self.y - other[1])
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector2D(self.x * other, self.y * other)
        else:
            return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, int):
            return Vector2D(self.x * other, self.y * other)
        else:
            return NotImplemented


class InclusiveBounds2D:
    def __init__(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        self.xmin = min(x1, x2)
        self.ymin = min(y1, y2)
        self.xmax = max(x1, x2)
        self.ymax = max(y1, y2)

    def __contains__(self, p):
        x, y = p
        return x >= self.xmin and x <= self.xmax and y >= self.ymin and y <= self.ymax

    def discrete_points(self):
        for y in range(self.ymin, self.ymax + 1):
            for x in range(self.xmin, self.xmax + 1):
                yield Vector2D(x, y)


EAST = Vector2D(1, 0)
WEST = Vector2D(-1, 0)
NORTH = Vector2D(0, -1)
SOUTH = Vector2D(0, 1)

RIGHT = Vector2D(1, 0)
LEFT = Vector2D(-1, 0)
UP = Vector2D(0, -1)
DOWN = Vector2D(0, 1)

ORIGIN = Vector2D(0, 0)
