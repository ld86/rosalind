#!/opt/local/bin/python3.2

from collections import Counter

lines = []

with open('input') as f:
    lines = f.read().split('\n')[1:-1:2]

cons = []

for i in range(0, len(lines[0])):
    counts = Counter([lines[j][i] for j in range(0, len(lines))])
    cons.append(counts.most_common(1)[0][0])

print("".join(cons))

for c in ["A", "C", "G", "T"]:
    line = ["%s:" % c]
    for i in range(0, len(lines[0])):
        counts = Counter([lines[j][i] for j in range(0, len(lines))])
        line.append(str(counts[c]))
    print(" ".join(line))
