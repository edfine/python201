def pos(func):
    # below is a nested, or inner function
    def new_function(*args, **kwargs):
        # do some stuff
        for arg in args:
            if arg > 0:
                # here we invoke the function passed in as an argument
                result = func(*args, **kwargs)
            else:
                print("not positive")
                result = None

        # do more stuff

        return result

    return new_function


@pos
def printer(s):
    print(s)
    return 0


printer(7)
printer(-15.6)