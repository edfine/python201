
class Mock:
    def __init__(self, retval = None):
        self.called = False
        self.params = ()
        self.retval = retval

    def __call__(self, *args, **kwargs):
        self.called = True
        self.params = (args, kwargs)
        return self.retval


