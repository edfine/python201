from polygon import Polygon

class Square(Polygon):
    def __init__(self):
        super().__init__(4)

    def inputSides(self):
        'only need one side length for a square'
        s = float(input("Enter length of side: "))
        'only need to store one side'
        self.sides = [s]

    def area(self):
        return self.sides[0] ** 2
