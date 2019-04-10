import unittest
from location import *

class TestLab1(unittest.TestCase):

#This case tests to see if repr prints out correctly
    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

#This next three cases test to see if eq works correctly by providing different values
#for the name, longitude, and latitude

    def test_eq(self):
        loc1 = Location("Yettem", 50.5, 30.2)
        loc2 = Location("Orosi", 60.5, 25.2)
        self.assertFalse(loc1 == loc2, False)
    def test_eq2(self):
        loc1 = Location("Yettem", 50.5, 30.2)
        loc2 = Location("Yettem", 50.5, 30.2)
        self.assertTrue(loc1==loc2, True)
    def test_eq3(self):
        loc1 = Location("Yettem", 50.5, 30.2)
        loc2 = Location("Culter", 55.5, 25.2)
        self.assertFalse(loc1==loc2, False)

if __name__ == "__main__":
        unittest.main()
