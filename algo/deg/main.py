import fileinput

edges = {}
points = []

for line in fileinput.input():
    a, b = line.strip().split()
    a, b = int(a), int(b)
    points.append((a,b))

    edges[a] = set()
    edges[b] = set()

for point in points:
    edges[point[0]].add(point[1])
    edges[point[1]].add(point[0])

print(edges)

print(" ".join(map(str,[len(edges[key]) for key in sorted(edges.keys())])))
