class Polygon():
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.sides = [0 for i in range(num_sides)]

    def __repr__(self):
        return ", ".join([str(i) for i in self.sides])

    def inputSides(self):
        self.sides = [float(input("Enter side "+ str(i + 1) + ": "))
                      for i in range(self.num_sides)]

    def area(self):
        print("Can't compute area of unknown polygon!")
        raise ValueError

