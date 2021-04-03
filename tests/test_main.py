from unittest import TestCase

from main import LiteralParser


class TestParser(TestCase):
    def setUp(self) -> None:
        self.parser = LiteralParser()
        with open("res/test_1.py", "r") as f:
            self.lines = f.readlines()


class TestFind(TestParser):
    def test_1(self):
        self.assertDictEqual(self.parser.find(self.lines), {'id': {0, 5}, 'value': {0, 6}})
