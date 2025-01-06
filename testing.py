import unittest

def addition(a,b):
    return a+b

class TestAddition(unittest.TestCase):

    def test_positive_number(self):
        result= addition(5,6)
        self.assertEqual(result,11)

    def test_negative_number(self):
        result= addition(-5,-6)
        self.assertEqual(result,-11)

if __name__=='__main__':
    unittest.main()

