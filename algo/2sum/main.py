import sys


def sum(a, i):
    a = zip(a, range(1, len(a) + 1))
    a.sort()
    l = 0
    r = len(a) - 1

    answer = None

    while l < r:
        e = a[l][0] + a[r][0]
        if e == i:
            answer = sorted([a[l][1], a[r][1]])
            r -= 1
            l += 1
        elif e > i:
            r -= 1
        else:
            l += 1

    if answer is not None:
        return answer

    return [-1]


def main():
    with open(sys.argv[1]) as f:
        k, _ = map(int, f.readline().split())
        for i in range(k):
            a = map(int, f.readline().split())
            print(" ".join(map(str, sum(a, 0))))


main()
