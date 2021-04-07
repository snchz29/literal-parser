from unittest import TestCase

from main import LiteralParser, RegExParser


class TestParser(TestCase):
    def setUp(self) -> None:
        self.parser_queue = LiteralParser()
        self.parser_regex = RegExParser()


class TestFind(TestParser):
    def test_queue_1(self):
        with open("res/test_1.py", "r") as f:
            self.assertDictEqual(self.parser_queue.find(f), {
                'id': [0, 5, 5],
                'value': [0, 6],
                'Hello world!': [2],
            })

    def test_queue_2(self):
        with open("res/test_2.py", "r") as f:
            self.assertDictEqual(self.parser_queue.find(f), {
                'abc \\"\\"': [0, 2],
                'def \\\\': [0, 2],
                'asdfasdf': [4],
            })

    def test_regex_1(self):
        with open("res/test_1.py", "r") as f:
            self.assertDictEqual(self.parser_queue.find(f), {
                'id': [0, 5, 5],
                'value': [0, 6],
                'Hello world!': [2],
            })

    def test_regex_2(self):
        with open("res/test_2.py", "r") as f:
            self.assertDictEqual(self.parser_queue.find(f), {
                'abc \\"\\"': [0, 2],
                'def \\\\': [0, 2],
                'asdfasdf': [4],
            })

    def test_time_1_queue(self):
        with open("res/test_3.py", "r") as f:
            self.parser_queue.find(f)

    def test_time_1_regex(self):
        with open("res/test_3.py", "r") as f:
            self.parser_regex.find(f)

    def test_time_2_queue(self):
        with open("res/test_3.py", "r") as f:
            self.parser_queue.find(f)

    def test_time_2_regex(self):
        with open("res/test_3.py", "r") as f:
            self.parser_regex.find(f)

    def test_time_3_queue(self):
        with open("res/test_3.py", "r") as f:
            self.parser_queue.find(f)

    def test_time_3_regex(self):
        with open("res/test_3.py", "r") as f:
            self.parser_regex.find(f)

    def test_time_4_queue(self):
        with open("res/test_3.py", "r") as f:
            self.parser_queue.find(f)

    def test_time_4_regex(self):
        with open("res/test_3.py", "r") as f:
            self.parser_regex.find(f)

    def test_time_5_queue(self):
        with open("res/test_3.py", "r") as f:
            self.parser_queue.find(f)

    def test_time_5_regex(self):
        with open("res/test_3.py", "r") as f:
            self.parser_regex.find(f)
