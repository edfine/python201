class MyObject(object):
    list_of_objects = []

    def __init__(self, name):
        self.name = name
        self.list_of_objects.append(name)

    def __del__(self):
        self.list_of_objects.remove(self.name)
