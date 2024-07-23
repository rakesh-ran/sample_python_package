import unittest
from sample_python_package.example_module import hello_world

class TestExampleModule(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, world!")

if __name__ == '__main__':
    unittest.main()
