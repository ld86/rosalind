#!/opt/local/bin/python3.2

import sys

def fib(n, k):
    if n == 0:
        return 1
    if n == 1:
        return 1

    return fib(n - 1, k) + k * fib(n - 2, k)

def main():
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    print(fib(n - 1,k))

main()
