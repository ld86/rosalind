import sys


def par(a):
    if len(a) == 1:
        return (a, 0)

    if len(a) == 2:
        if a[0] > a[1]:
            return (a, 1)
        else:
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


def find_k(a, k):
    if len(a) == 1 and k == 1:
        return a[0]

    a, l = par(a)
    left = a[:l + 1]
    right = a[l + 1:]
    if k <= len(left):
        return find_k(left, k)
    else:
        return find_k(right, k - len(left))


def main():
    with open(sys.argv[1]) as f:
        f.readline()
        a = map(int, f.readline().split())
        k = int(f.readline())
        print(find_k(a, k))

main()
