class MyRandomIterator(object):
    def __init__(self, iterable):
        import random
        self.iterable = list(iterable)
        random.shuffle(self.iterable)
        self.pos = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.pos < len(self.iterable):
            self.pos += 1
            return self.iterable[self.pos - 1]
        else:
            raise StopIteration
        
if __name__ == "__main__":        
    mri = MyRandomIterator('I have learned a lot in this class!')
    for item in mri:
        print(item, end=' ')
