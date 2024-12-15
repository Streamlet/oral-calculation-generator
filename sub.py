import random
import argparse


def generate(nums, min_sum, max_sum):
    for i in range(min_sum, max_sum + 1):
        if nums - 1 <= 0:
            yield (i,)
        else:
            for t in generate(nums - 1, min_sum, max_sum - i):
                yield (i, *t)


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-m', '--min', default=0, type=int)
    parser.add_argument('-M', '--max', default=10, type=int)
    parser.add_argument('-c', '--count', type=int)
    args = parser.parse_args()

    expressions = []
    for t in generate(2, args.min, args.max):
        expressions.append('%-2d-%2d =' % (sum(t), t[0]))
    if args.count is not None:
        while (len(expressions) < args.count):
            expressions = expressions * ((args.count - 1) // len(expressions) + 1)
    random.shuffle(expressions)
    if args.count is not None:
        expressions = expressions[:args.count]
    for expression in expressions:
        print(expression)


if __name__ == '__main__':
    main()
