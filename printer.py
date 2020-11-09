def counterwrap(func):
    def inner(s):
        from collections import Counter
        count = Counter(s)
        for item in count:
            print(item, count[item])
        print('    about to execute', func)
        func(s)
    
    return inner

@counterwrap
def printer(s):
    print(s)

printer('mississippi')
#once_decorated_printer = counterwrap(printer)
#twice_decorated_printer = counterwrap(once_decorated_printer)

#print("Executing once_decorated_printer...")
#once_decorated_printer('hello')
#print()
#print("Executing twice_decorated_printer...")
#twice_decorated_printer('hello')

