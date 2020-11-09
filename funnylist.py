class FunnyList(list):
    def __init__(self, item):
        """Allows us to create a FunnyList not only from a list,
           but ALSO from a single element
        """
        if type(item) == list:
            return super().__init__(item)
        else:
            return super().__init__([item])

    def __eq__(self, other):
        """Check for equality without concern for order.
           If the sorted versions of two FunnyLists are the
           same, then we deem the FunnyLists to be the same.
        """
        return sorted(self) == sorted(other)

    def __ne__(self, other):
        return sorted(self) != sorted(other)

    def __add__(self, thing):
        """Add to a FunnyList. Distinguish between adding a
           list/FunnyList, and something else.
        """
        if not isinstance(thing, list):
            return FunnyList(super().__add__([thing]))

        return FunnyList(super().__add__(thing))
    
    def __iadd__(self, thing):
        """Same as above except this is += instead of +."""
        return self + thing
