import unittest
import prime


class TestPrime(unittest.TestCase):
    def test_add(self):
        self.assertEqual(prime.add(7, 8), 15)

    def test_multiply(self):
        self.assertEqual(prime.multiply(5, 8), 40)


if __name__ == '__main__':
    unittest.main()
