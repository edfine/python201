from typing import List, Any

def func(arg: int) -> List[int]:
    '''This function takes an int and returns a list of ints'''
    mylist: List[int] = []
    x: int = 3.0 # oops!
    mylist.append(x)

    return mylist

def otherfunc(arg: float) -> List[Any]:
    '''This function takes a float and return any kind of list'''
    return str(arg)
