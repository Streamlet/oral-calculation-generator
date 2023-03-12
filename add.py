import sys
import random


def generate(sum_upper_bound):
    for i in range(sum_upper_bound + 1):
        for j in range(sum_upper_bound + 1 - i):
            yield (i, j)


def main():
    sum_upper_bound = 100
    if len(sys.argv) > 1:
        sum_upper_bound = int(sys.argv[1])
    expressions = []
    for (i, j) in generate(sum_upper_bound):
        expressions.append('%d + %d =' % (i, j))
    random.shuffle(expressions)
    for expression in expressions:
        print(expression)


if __name__ == '__main__':
    main()
