from collections import defaultdict
import sys

counts = defaultdict(lambda: 0)
for c in open('rosalind_dna.txt').read()[:-1]:
    counts[c] += 1
for key in sorted(counts.keys()):
    sys.stdout.write(str(counts[key]) + " ")
