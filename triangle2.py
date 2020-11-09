from triangle import Triangle

class EquiTriangle(Triangle):
    def __init__(self):
        '''
        use super() to call __init__ in base class and
        be sure we have 3 sides
        '''
        super().__init__()

    def inputSides(self):
        'only need one side length for a square'
        s = float(input("Enter length of side: "))
        'only need to store one side'
        self.sides = [s] * 3
    
