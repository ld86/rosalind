import sys
import Queue


def bfs(start, edges, distance):
    queue = Queue.Queue()
    queue.put((start, 0))
    seen = [False] * len(distance)
    seen[0] = True
    while not queue.empty():
        a = queue.get()
        distance[a[0]] = a[1]
        for b in edges[a[0]]:
            if seen[b] is False:
                queue.put((b, a[1] + 1))
                seen[b] = True


def main():
    with open(sys.argv[1]) as f:
        n, m = map(int, f.readline().split())
        edges = [[] for i in range(n)]
        distance = [-1] * n
        for i in range(m):
            a, b = map(int, f.readline().split())
            edges[a - 1].append(b - 1)
        bfs(0, edges, distance)
        print(" ".join(map(str, distance)))

main()
