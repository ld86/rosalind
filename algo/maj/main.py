import sys


def binary(q, a):
    l, r = 0, len(a)
    while l < r:
        mid = (r + l) // 2
        if a[mid] < q:
            l = mid + 1
        elif a[mid] > q:
            r = mid
    return l


def is_popular(i, a):
    l = binary(i - 0.1, a)
    r = binary(i + 0.1, a)
    return r - l > len(a) // 2


def main():
    answers = []
    with open(sys.argv[1]) as f:
        n, k = map(int, f.readline().split())
        for i in range(0, n):
            a = map(int, f.readline().split())
            a.sort()
            popular = -1
            for i in [a[0], a[-1], a[len(a) // 2]]:
                if is_popular(i, a):
                    popular = i
                    break
            answers.append(popular)

    print(" ".join(map(str, answers)))

main()
