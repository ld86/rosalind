import sys


def merge(a, b):
    result = []
    ap = bp = 0
    while ap != len(a) and bp != len(b):
        if a[ap] <= b[bp]:
            result.append(a[ap])
            ap += 1
        else:
            result.append(b[bp])
            bp += 1

    if ap != len(a):
        result.extend(a[ap:])
    elif bp != len(b):
        result.extend(b[bp:])

    return result


def main():
    with open(sys.argv[1]) as f:
        f.readline()
        a = map(int, f.readline().split())
        f.readline()
        b = map(int, f.readline().split())
        print(" ".join(map(str, merge(a, b))))

main()
