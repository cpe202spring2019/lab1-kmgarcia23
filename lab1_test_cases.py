import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        # This case tests when the list is none
        tlist = None
        with self.assertRaises(ValueError):
            max_list_iter(tlist)

        # This case tests the recursion
        tlist = [3,4,5,2,8]
        self.assertEqual(max_list_iter(tlist),4)

        # This case tests when the list is empty
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)

    def test_reverse_rec(self):
        # This cases tests the recursion
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

        # This case tests when the list is None
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)

    def test_bin_search(self):
        # This case tests when the list is None
        list_val = None
        low = 0
        high = 2
        with self.assertRaises(ValueError):
            bin_search(2, low, high, list_val)

        # This case tests when the target is in the middle
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), 4 )

        # This case tests when the target is below the middle
        list_val = [0,1,2,3,4,5]
        low = 0
        high = len(list_val) -1
        self.assertEqual(bin_search(1,low,high,list_val),1)

        # This case tests when the target is higher than the middle
        list_val = [1,2,3,4,5]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(5,low,high,list_val),4)

        # This case tests when the target isn't in the list at all
        list_val = [1,2,3,4,5,6,7]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(8,low,high,list_val),None)

if __name__ == "__main__":
        unittest.main()
