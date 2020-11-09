class MyDefaultDict(dict):
    def __init__(self, type):
        self.dict = {}
        if type == int:
            self.default = 0
           
    def __getitem__(self, key):
        return self.get(key)

    def get(self, key):
        if key in self.dict:
            return self.dict[key]
        else:
            return self.default
