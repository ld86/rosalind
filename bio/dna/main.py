from collections import Counter

counts = Counter(open('rosalind_dna.txt').read()[:-1])
print(" ".join([str(counts[key]) for key in sorted(counts.keys())]))
