class FunnyList(list):
    def __eq__(self, other):
        """Check for equality without concern for order.
           If the sorted versions of two FunnyLists are the
           same, then we deem the FunnyLists to be the same."""
        return sorted(self) == sorted(other)
    
    def __add__(self, thing):
        """Add an item to a FunnyList. We'll create a new list
           which is a copy of our current list (self) plus the
           item we want to add.
        """
        newlist = self.copy() + [thing]

        return FunnyList(newlist)
