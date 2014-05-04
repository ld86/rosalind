#!/opt/local/bin/python3.2

import sys
import array

def binary(q, a):
    l, r = 0, len(a)
    while l < r:
        mid = (r + l) // 2
        if a[mid] < q:
            l = mid + 1
        elif a[mid] > q:
            r = mid
        else:
            return mid + 1
    return -1

n, k, a, b = open('input').read().split('\n')[:-1]
n, k = int(n), int(k)
a = array.array('l', map(int, a.split(' ')))
b = map(int, b.split(' '))
print(" ".join([str(binary(q, a)) for q in b]))
