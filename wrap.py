def validate_args(f):
    def check_args(arg, **kwargs):
        if arg < 0:
            arg = -arg
        f(arg)

    return check_args

@validate_args
def func(x):
    '''x must be positive'''
    print(x)

func(-5)

