import re
import sys
from collections import deque
from typing import List, Iterable, Dict, Deque, Callable, Set


def select_non_unique_literals(fn: Callable) -> Callable:
    def wrapper(lines: Iterable[str]) -> Dict[str, Set[int]]:
        return {key: set(val) for key, val in fn(lines).items() if len(val) > 1}
    return wrapper


class LiteralParser():
    """
    Pulls all string literals except
    multiline literals, f-strings, and comment literals.
    """

    def _find_literals(self, line: str) -> List[str]:
        queue = deque()
        index = 0
        length = len(line)
        while index < length:
            if line[index] == "#":  # beginning of one-line comment
                return self.split_line(line, queue)
            if line[index] == "'" or line[index] == '"':
                quote = line[index]
                index += 1
                queue.append(index)
                # Iterating over the line until a closing unescaped quote is found
                while index < length and line[index] != quote:
                    if line[index] == "\\":
                        index += 1
                    index += 1
                # Check if the found symbol is quote, not EOL
                if index < length:
                    queue.append(index)
            index += 1
        if len(queue) % 2:
            raise SyntaxError(f"There is no closing quote symbol for quote at index {queue.pop()} "
                              f"in line: \n{line}")
        return self.split_line(line, queue)

    def find(self, file: Iterable[str]) -> Dict[str, List[int]]:
        all_results = dict()
        line_number = 0
        for line in file:
            for literal in self._find_literals(line):
                all_results.setdefault(literal, []).append(line_number)
            line_number += 1
        return all_results

    @staticmethod
    def split_line(line: str, queue: Deque[int]) -> List[str]:
        result = []
        while len(queue):
            b_index = queue.popleft()
            e_index = queue.popleft()
            result.append(line[b_index:e_index])
        return result

class RegExParser(LiteralParser):
    def _find_literals(self, line: str) -> List[str]:
        # select group 2 (literal) if group 3 (comment) is empty
        #                                      |  1  ||                2                 |   | 3 |
        return [lit[1] for lit in re.findall(r"(['\"])((?:(?:[^\\])*?(?:\\.)*(?:\\\\)*)*?)\1|(#.*)", line) if len(lit[2])==0]

def main():
    parser = LiteralParser()
    parser.find = select_non_unique_literals(parser.find)
    try:
        with open(sys.argv[1]) as f:
            results = parser.find(f)
            print(*[f"Lines with '{key}': {', '.join(map(str, val))}" for key, val in results.items()], sep="\n")
    except IOError as e:
        print(e, file=sys.stderr)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Fatal error: No input files", file=sys.stderr)
    else:
        if len(sys.argv) > 2:
            print("Warning: Too much input files. Only first one will be parsed.", file=sys.stderr)
        main()
