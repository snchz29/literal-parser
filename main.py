import re
import sys
from collections import deque


class LiteralParser:
    def __init__(self, filename: str):
        self.__filename = filename

    def _read_file(self) -> list:
        with open(self.__filename, 'r') as f:
            res = f.read()
        return res.split("\n")

    def __filter(self, dict_: dict) -> dict:
        result = dict_.copy()
        for key, val in dict_.items():
            result.update({key: set(val)})
            if len(val) < 2:
                result.pop(key)
        return result

    def _find_literals(self, line: str) -> list:
        pass

    def find(self) -> dict:
        all_results = dict()
        line_number = 0
        for line in self._read_file():
            for literal in self._find_literals(line):
                all_results.setdefault(literal, []).append(line_number)
            line_number += 1
        return self.__filter(all_results)


class RegEXParser(LiteralParser):
    def _find_literals(self, line: str) -> list:
        return [lit[1] for lit in re.findall(r"([\"'])(.*?)\1", line)]


class DequeParser(LiteralParser):
    def _find_literals(self, line: str) -> list:
        queue = deque()
        line_iter = iter(line)
        result = []
        char = next(line_iter, None)
        while char:
            if char == "'" or char == '"':
                quote = char
                char = next(line_iter, None)
                while char and char != quote:
                    queue.append(char)
                    char = next(line_iter, None)
                result.append("".join(queue))
                queue.clear()
            char = next(line_iter, None)
        return result


if __name__ == '__main__':
    if len(sys.argv) == 2:
        explorer = DequeParser(sys.argv[1])
        results = explorer.find()
        print(*[f"Lines with '{key}': {', '.join(map(str, val))}" for key, val in results.items()], sep="\n")
    else:
        print("Fatal error: No input files")
