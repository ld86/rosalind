#!/opt/local/bin/python3.2

import sys
import fileinput

dnas = []
label = ''
dna = ''

for line in fileinput.input():
    line = line.strip()

    if line[0] == '>':
        if label != '':
            dnas.append(( (dna.count('G') + dna.count('C')) / len(dna) * 100, label, dna))
        label = line
        dna = ''
        continue

    dna += line

dnas.append(( (dna.count('G') + dna.count('C')) / len(dna) * 100, label, dna))
print(dnas)
result = max(dnas)
print(result[1])
print(result[0])
