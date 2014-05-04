#!/opt/local/bin/python3.2

import sys

n = int(sys.argv[1])

a, b = 0, 1
for i in range(0, n):
    a, b = b, a + b
print(a)
