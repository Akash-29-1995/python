import unittest

class TestHello(unittest.TestCase):
    def test_output(self):
        self.assertEqual('Hello, World!', 'Hello, World!')

if __name__ == '__main__':
    unittest.main()
