#!/opt/local/bin/python3.2

import sys

def main():
    n = int(sys.argv[1])
    k = int(sys.argv[2])

    r = [0 for i in range(0,k + 1)]
    r[0] = 1
    for i in range(0, n - 1):
        r[1:k + 1] = r[:k]
        r[0] = sum(r[2:k+1])
        r[k] = 0
    print(sum(r))

main()
