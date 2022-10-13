class Example:
    """add class methods to your class which keeps track of all the instance names which have been created
    allnames() should return a list of all the names of objects which exist
    count() should return the number of objects that have ever been created
    we will need __del__ to accomplish this
    """
    __some_data = 'blah'
    __how_many = 0
    __instance_names = []
    __ever_created = 0
    
    def __init__(self, val):
        print('in init for Example')
        self.name = val # instance data
        self.__class__.__how_many += 1 # get from object to class
        self.__class__.__ever_created += 1 # get from object to class
        self.__class__.__instance_names.append(val)
        print('__how_many =', self.__class__.__how_many)

    def __del__(self):
        self.__class__.__instance_names.remove(self.name)
        self.__class__.__how_many -= 1
        
    # We can use a static (or class) method to get around
    # a brittle __init__ that doesn't quite do what we want.
    @staticmethod
    def list_init(somelist):
        '''allow me to send in a list, and "flatten" it
        into a string with intervening commas'''
        obj = Example('')
        obj.name = ', '.join(somelist)
        return obj
    
    @classmethod
    def get_some_data(cls):
        return cls.__some_data

    @classmethod
    def allnames(cls):
        return cls.__instance_names

    @classmethod
    def count_current(cls):
        return cls.__how_many

    @classmethod
    def count_ever(cls):
        return cls.__ever_created

if __name__ == '__main__':
    print("put tests here to make sure I did the lab right.")
    ex1 = Example('example1')
    ex2 = Example('example2')
    print(Example.allnames())
    print(ex2.count_current())
    ex3 = Example('example3')
    print(ex3.count_current())
    print(ex3.count_ever())
    del ex3
    print(Example.count_current())
    print(Example.count_ever())
    print(ex1.allnames())

    

