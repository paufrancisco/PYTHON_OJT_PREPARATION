import unittest

def multiply(x,y):
    return x*y

class TestMath(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(3,4),12)
        self.assertEqual(multiply(-1,5),-5)

if __name__== '__main__':
    unittest.main()