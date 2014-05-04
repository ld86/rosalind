#!/opt/local/bin/python3.2

import sys

argv = sys.argv[1:]

argv[0] = 2 * float(argv[0])
argv[1] = 2 * float(argv[1])
argv[2] = 2 * float(argv[2])
argv[3] = 2 * float(argv[3]) * 3 / 4
argv[4] = 2 * float(argv[4]) * 1 / 2
argv[5] = 0

print(sum(argv))
