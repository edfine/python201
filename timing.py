import time


def timing(func):
    # below is a nested, or inner function
    def new_function(*args, **kwargs):
        # do some stuff
        tstart = time.time()
        result = func(*args, **kwargs)

        # do more stuff
        tend = time.time()
        print(tend - tstart)
        return result

    return new_function


@timing
def printer(s):
    print(s)


printer(98)