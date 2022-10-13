import random

class Myrandomiterator():
    
    def __init__(self, iterable):
        self.rand_iterable = random.shuffle(list(iterable))
        self.remaining = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        """ 
        each call to next() does two important things:

        1. modify its state for the subsequent next() call
        2. produces a result for the current call
        """
        
        if self.remaining > 0:
            self.remaining -= 1
            value = self.rand_iterable.pop()
            return value
        else:
            raise StopIteration

if __name__ == "__main__":        
    mri = MyRandomIterator('I think I'll go to the zoo!')
    for item in mri:
        print(item, end=' ')