from random import Random

class ZanyInt(int):
    def __len__(self):
        return len(str(self))

    def str(self):
        if self == 3:
            return "three"
        else:
            return '    ' + super.__str__(self)

    def __add__(self, other):
        if Random.random > 0.5:
            return "Gotcha"
        else:
            sum = super().__add__(other)
            return sum

if __name__ == "__main__":
    pass