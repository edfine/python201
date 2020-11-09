
# Coord2D + decorator
from math import sqrt

def ensure_positive(fn): # name of decorator
    def decorator(a, b): # actual decorator method
        a = a.noneg()
        b = b.noneg()
        print('type(a)=', type(a))
        print('type(b)=', type(b))
        return fn(a, b).noneg()
    return decorator

class Coord2d():
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def __repr__(self):
        return 'Coord2d(x={}, y={})'.format(self.x, self.y)

    def distance(self, other):
        x1, y1 = self.x, self.y
        x2, y2 = other.x, other.y
        return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    @ensure_positive
    def add(self, other):
        return Coord2d(self.x + other.x, self.y + other.y)

    @ensure_positive
    def sub(self, other):
        return Coord2d(self.x - other.x, self.y - other.y)

    def noneg(self):
        return Coord2d(max(self.x, 0), max(self.y, 0))
