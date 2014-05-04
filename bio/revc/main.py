Mapping = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
print("".join(map(lambda x: Mapping[x], reversed(open('rosalind_revc.txt').read()[:-1]))))
