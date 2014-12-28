import sys


def main():
    with open(sys.argv[1]) as f:
        n, m = map(int, f.readline().split())
        edges = [[] for i in range(n)]
        for i in range(m):
            a, b = map(int, f.readline().split())
            edges[a - 1].append(b - 1)
            edges[b - 1].append(a - 1)
        answer = [sum([len(edges[i]) for i in edges[j]]) for j in range(n)]
        print(" ".join(map(str, answer)))

main()
