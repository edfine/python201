from polygon import Polygon

class Triangle(Polygon):
    def __init__(self):
        '''
        use super() to call __init__ in base class and
        be sure we have 3 sides
        '''
        super().__init__(3)

    def area(self):
        import math
        a, b, c = self.sides
        'compute semi-perimeter'
        s = sum(self.sides) / 2
        "compute area using Heron's formula"
        area = math.sqrt((s * (s - a) * (s - b) * (s - c)))
        return area

print('I am in triangle.py')
