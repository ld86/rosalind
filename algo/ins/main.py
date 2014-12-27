import sys


def insertion_sort(a):
    swaps = 0
    for i in range(1, len(a)):
        k = i
        while k > 0 and a[k] < a[k - 1]:
            a[k - 1], a[k] = a[k], a[k - 1]
            k -= 1
            swaps += 1
    return swaps


def main():
    with open(sys.argv[1]) as f:
        f.readline()
        a = map(int, f.readline().split())
        print(insertion_sort(a))

main()
