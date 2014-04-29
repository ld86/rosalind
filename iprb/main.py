#!/opt/local/bin/python3.2

import sys

k = int(sys.argv[1])
m = int(sys.argv[2])
n = int(sys.argv[3])

kk = k / (k + m + n) * (k - 1) / (k + m + n -1) * 1
mm = m / (k + m + n) * (m - 1) / (k + m + n -1) * 3/4
nn = n / (k + m + n) * (n - 1) / (k + m + n -1) * 0

km = 2 * k / (k + m + n) * m / (k + m + n - 1) * 1
kn = 2 * k / (k + m + n) * n / (k + m + n - 1) * 1
mn = 2 * m / (k + m + n) * n / (k + m + n - 1) * 1/2

print(kk + mm + nn + km + kn + mn)
