from unittest import TestCase

from main import LiteralParser, RegExParser


class TestParser(TestCase):
    def setUp(self) -> None:
        self.parser_queue = LiteralParser()
        self.parser_regex = RegExParser()


class TestFind(TestParser):
    def test_1_queue(self):
        with open("res/test_3.py", "r") as f:
            self.parser_queue.find(f)

    def test_1_regex(self):
        with open("res/test_3.py", "r") as f:
            self.parser_regex.find(f)

    def test_2_queue(self):
        with open("res/test_3.py", "r") as f:
            self.parser_queue.find(f)

    def test_2_regex(self):
        with open("res/test_3.py", "r") as f:
            self.parser_regex.find(f)

    def test_3_queue(self):
        with open("res/test_3.py", "r") as f:
            self.parser_queue.find(f)

    def test_3_regex(self):
        with open("res/test_3.py", "r") as f:
            self.parser_regex.find(f)

    def test_4_queue(self):
        with open("res/test_3.py", "r") as f:
            self.parser_queue.find(f)

    def test_4_regex(self):
        with open("res/test_3.py", "r") as f:
            self.parser_regex.find(f)

    def test_5_queue(self):
        with open("res/test_3.py", "r") as f:
            self.parser_queue.find(f)

    def test_5_regex(self):
        with open("res/test_3.py", "r") as f:
            self.parser_regex.find(f)
