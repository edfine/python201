
class Foo():
    class FooException(Exception):
        pass

    my_exception = FooException('test')

from unittest.mock import Mock

m = Mock(spec=Foo, side_effect = Foo.FooException)


