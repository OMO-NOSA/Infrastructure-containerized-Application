import unittest
from factorial import factorial

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.factorial = factorial
        

    def test_valid_factorial(self):
        self.assertEqual(120, self.factorial(5))
        self.assertEqual(1, self.factorial(1))
        self.assertEqual(1, self.factorial(0))
        self.assertEqual(30414093201713378043612608166064768844377641568960512000000000000, self.factorial(50.0))
        
    def test_invalid_factorial(self):
        self.assertEqual('Invalid Input', self.factorial(-1))
        self.assertEqual('Invalid Input', self.factorial('fib'))
        

if __name__ == '__main__':
    unittest.main()