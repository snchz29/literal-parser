import re
import sys
from collections import deque


class LiteralParser:
    def __init__(self, filename: str):
        self.__filename = filename

    def _read_file(self) -> list:
        with open(self.__filename, 'r') as f:
            lines = f.readlines()
        return lines

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
        index = 0
        length = len(line)
        while index < length:
            if line[index] == "'" or line[index] == '"':
                quote = line[index]
                index += 1
                queue.append(index)
                while index < length and (line[index] != quote or index > 0 and line[index-1] == "\\"):
                    index += 1
                queue.append(index)
            index += 1
        return split_line(line, queue)


def split_line(line:str, queue:deque)->list:
    result = []
    while len(queue):
        b_index = queue.popleft()
        e_index = queue.popleft()
        result.append(line[b_index:e_index])
    return result


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Fatal error: No input files")
    elif len(sys.argv) > 2:
        print("Warning: Too much input files. Only first one will be parsed.")

    explorer = DequeParser(sys.argv[1])
    results = explorer.find()
    print(*[f"Lines with '{key}': {', '.join(map(str, val))}" for key, val in results.items()], sep="\n")
