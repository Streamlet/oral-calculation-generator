import sys
import random


def generate(nums, lower_bound, upper_bound):
    for i in range(lower_bound, upper_bound + 1):
        if nums - 1 <= 0:
            yield (i,)
        else:
            for t in generate(nums - 1, lower_bound, upper_bound - i):
                yield (i, *t)

def main():
    lower_bound = 0
    upper_bound = 100
    if len(sys.argv) > 1:
        lower_bound = int(sys.argv[1])
    if len(sys.argv) > 2:
        upper_bound = int(sys.argv[2])
    expressions = []
    for t in generate(2, lower_bound, upper_bound):
        expressions.append('%-2d+%2d =' % (t[0], t[1]))
        expressions.append('%-2d-%2d =' % (sum(t), t[0]))
    random.shuffle(expressions)
    for expression in expressions:
        print(expression)


if __name__ == '__main__':
    main()
