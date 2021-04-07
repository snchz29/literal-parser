from random import randint

letters = ["a", "b", "c"]

for lines in range(50000):
    for literal in range(20):
        print("\"" + "".join([letters[randint(0, 2)] for _ in range(randint(3, 10))]) + "\"", sep="", end=" ")
    print()
