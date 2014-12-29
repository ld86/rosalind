import sys
import Queue


def bfs(start, edges, components):
    queue = Queue.Queue()
    next_component = max(components) + 1
    queue.put(start)
    seen = [False] * len(components)
    seen[start] = True
    while not queue.empty():
        a = queue.get()
        components[a] = next_component
        for b in edges[a]:
            if seen[b] is False:
                queue.put(b)
                seen[b] = True


def main():
    with open(sys.argv[1]) as f:
        n, m = map(int, f.readline().split())
        edges = [[] for i in range(n)]
        components = [-1] * n
        for i in range(m):
            a, b = map(int, f.readline().split())
            edges[a - 1].append(b - 1)
            edges[b - 1].append(a - 1)
        for v, c in enumerate(components):
            if c == -1:
                bfs(v, edges, components)
        print(len(set(components)))

main()
