from dataclasses import dataclass


@dataclass(frozen=True)
class Vector2D:
    x: int
    y: int

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
