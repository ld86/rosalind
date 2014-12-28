import sys


def sum(a, i):
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
            a = zip(a, range(1, len(a) + 1))
            a.sort()

            answer = None
            for i, e in enumerate(a):
                sum2 = sum(a, -e[0])
                if sum2[0] != -1:
                    sum2.append(e[1])
                    answer = sum2
                    break
            if answer is not None:
                print(" ".join(map(str, sorted(answer))))
            else:
                print("-1")

main()
