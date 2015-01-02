import sys


def par(a):
    if len(a) == 1:
        return (a, 0)

    p = a[0]
    l = 1
    r = len(a) - 1

    while l < r:
        while a[l] <= p:
            l += 1
        while a[r] > p:
            r -= 1
        if l < r:
            a[l], a[r] = a[r], a[l]
    a[0], a[r] = a[r], a[0]
    position = r

    l = 0
    r -= 1

    while l < r:
        if a[l] == p:
            a[l], a[r] = a[r], a[l]
            r -= 1
        else:
            l += 1

    return (a, position)


def qs(a):
    if len(a) <= 10:
        return sorted(a)
    a, l = par(a)
    return qs(a[:l + 1]) + qs(a[l + 1:])


def main():
    with open(sys.argv[1]) as f:
        f.readline()
        a = map(int, f.readline().split())
        print(" ".join(map(str, qs(a))))

main()
