from collections import Counter

def count_characters(func):
    # below is a nested, or inner function
    def inner_function(mystr): 
        # some business logic
        chars = Counter(mystr)
        print(chars)

        # here we invoke the function passed in as an argument
        result = func(mystr)

        # some more business logic
        return result
    
    # my_decorator_name() returns a reference to the inner function
    return inner_function

# This is the general pattern I use for writing simple decorators
def my_decorator_name(func):
    # below is a nested, or inner function
    def inner_function(*args, **kwargs): 
        # some business logic

        # here we invoke the function passed in as an argument
        result = func(*args, **kwargs)

        # some more business logic
        return result
    
    # my_decorator_name() returns a reference to the inner function
    return inner_function

@count_characters
def printer(mystring):
    print(mystring)

#myprint = count_characters(printer)
printer('hello world')

printer("Python")