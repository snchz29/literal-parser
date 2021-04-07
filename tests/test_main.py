from unittest import TestCase

from main import LiteralParser


class TestParser(TestCase):
    def setUp(self) -> None:
        self.parser = LiteralParser()


class TestFind(TestParser):
    def test_1(self):
        with open("res/test_1.py", "r") as f:
            self.assertDictEqual(self.parser.find(f), {
                'id': [0, 5, 5],
                'value': [0, 6],
                'Hello world!': [2],
            })

    def test_2(self):
        with open("res/test_2.py", "r") as f:
            self.assertDictEqual(self.parser.find(f), {
                'abc \\"\\"': [0, 2],
                'def \\\\': [0, 2],
                'asdfasdf': [4],
            })

