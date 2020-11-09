from string import ascii_lowercase
import random

class ListMe():
    all_names = []

    def __init__(self, name):
        if name in self.__class__.all_names:
            while name in self.__class__.all_names:
                name = ''.join([random.choice(ascii_lowercase)
                                for ltr in range(6)])
            print('Your name is in use so changed it to "%s"'
                   % name)
        self.name = name
        self.__class__.all_names.append(name)
 
    def __del__(self):
        print('in ListMe.del()')
        self.__class__.all_names.remove(self.name)

    @classmethod
    def listAllNames(cls):
        print(cls.all_names)

