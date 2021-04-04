# Literal Parser

Simple program for finding non-unique string literals in python files.

## Getting started

```
git clone https://github.com/snchz29/literal-parser.git
cd literal-parser
python3 main.py [filename]
```

Where `[filename]` is the path to the file for analysis.

## Algorithm

This implementation is based on the use of a queue. 

Class LiteralParser processes a list of strings and returns a dictionary in which the key is an all literals, and the value is a list of line numbers.

For each line, the index of each quote is enqueued.
Quotes in comments are ignored.
Obviously, for, each line must contain an even number of quotes, so an exception is thrown if there is an odd number of quotes.

After that, the line is split by indices from the queue.

To filter only non-unique literals, use the appropriate decorator for the find function.

## Example

File content for parsing:

```python
database = [{'id': i, "value": str(i)} for i in range(100)]

print("Hello world!")

for data in database:
    if data['id'] % 10 == 0 or data['id'] == 13:
        print(data['value'])
```

Program output:

```
Lines with 'id': 0, 5
Lines with 'value': 0, 6
```