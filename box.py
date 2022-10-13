from dataclasses import dataclass

class Box:
  def __init__(self):
    raise ValueError('cannot instantiate "Box"')

  def count_items(self):
    return len(self.items)

  def list_items(self):
    for item in self.items:
      print(str(item))

  def empty(self):
    raise NotImplementedError()

  def add_item(self, item):
    raise NotImplementedError()

@dataclass
class Item:
  name: str
  price: float

class ListBox(Box):
  def __init__(self):
    self.items = []

  def empty(self):
    self.items = []

  def add_item(self, item):
    self.items.append(item)

class DictBox(Box):
  def __init__(self):
    self.items = {}

  def empty(self):
    self.items = {}

  def add_item(self, item):
    self.items[item.name] = item

lb = ListBox()
db = DictBox()

lb.add_item(Item('book', 10.0))
lb.add_item(Item('computer', 999.99))
lb.list_items()

db.add_item(Item('phone', 500.00))
db.add_item(Item('pencil', 1.00))
db.list_items()