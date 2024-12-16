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


EAST = Vector2D(1, 0)
WEST = Vector2D(-1, 0)
NORTH = Vector2D(0, -1)
SOUTH = Vector2D(0, 1)
