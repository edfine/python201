from funnylist import FunnyList
import unittest

class TestFunnyList(unittest.TestCase):
    
    def setUp(self):
        # create two standard Python lists
        self.list1 = [1, 2, 3]
        self.list2 = [3, 2, 1]
        # create a combined list of the above
        self.clist = self.list1 + self.list2
        # create two FunnyLists from the lists
        self.fl1 = FunnyList(self.list1)
        self.fl2 = FunnyList(self.list2)
    
    def test_equal(self):
        """Check for equality."""
        self.assertTrue(self.fl1 == self.fl2)

    def test_add_two(self):
        """Check that adding two FunnyLists together
           yields the same result as adding two lists
           together.
        """ 
        self.fl3 = self.fl1 + self.fl2
        self.assertEqual(self.fl3, self.clist)

    def test_add_int(self):
        """Check that we can add an integer to a FunnyList."""
        self.fl3 = self.fl1 + 10
        self.list1.append(10)
        self.assertEqual(self.fl3, self.list1)

unittest.main()


