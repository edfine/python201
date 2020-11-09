class First(object):
  def __init__(self):
    print("in first __init__")
    super().__init__()
    print("first")

class Second(object):
  def __init__(self):
    print("in second __init__")
    super().__init__()
    print("second")

class Third(First, Second):
  def __init__(self):
    print("in third __init__")
    super().__init__()
    print("third")

print(Third.__mro__)
t = Third()
