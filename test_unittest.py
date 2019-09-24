import unittest

class MyTestCase(unittest.TestCase):
    items = []

    @classmethod
    def setUpClass(cls):
        cls.items.append("hello")

    @classmethod
    def tearDownClass(cls):
        cls.items.pop()

    def setUp(self):
        self.number = 1

    def tearDown(self):
        self.number = None

    def test_method1(self):
        assert self.number == 1
        assert self.items[0] == "hello"

    def test_method2(self):
        assert self.number == 1
        assert self.items[0] == "hello"
