import sys
import random

inverses = 0


def merge(a, b):
    global inverses
    result = []
    ap = bp = 0

    while ap != len(a) and bp != len(b):
        if a[ap] <= b[bp]:
            result.append(a[ap])
            ap += 1
        else:
            inverses += len(a[ap:])
            result.append(b[bp])
            bp += 1

    if ap != len(a):
        result.extend(a[ap:])
    elif bp != len(b):
        result.extend(b[bp:])

    return result


def sort(a):
    if len(a) <= 1:
        return a

    middle = len(a) // 2
    b = sort(a[:middle])
    c = sort(a[middle:])
    return merge(b, c)


def naive(a):
    c = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if i < j and a[i] > a[j]:
                c += 1
    return c


def random_array(n):
    return [random.randint(0, 10) for i in range(n)]


def main():
    global inverses
    with open(sys.argv[1]) as f:
        f.readline()
        a = map(int, f.readline().split())
        sort(a)
        print(inverses)


main()
