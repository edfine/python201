class FunnyList(list):
    def __eq__(self, other):
        """Check for equality without concern for order.
           If the sorted versions of two FunnyLists are the
           same, then we deem the FunnyLists to be the same.
        """
        return sorted(self) == sorted(other)
    
