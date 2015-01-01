import sys


def add(heap, a):
    heap.append(a)
    c = len(heap) - 1
    while c != 0:
        p = (c - 1) / 2
        if heap[p] >= heap[c]:
            break
        heap[p], heap[c] = heap[c], heap[p]
        c = p


def main():
    with open(sys.argv[1]) as f:
        f.readline()
        a = map(int, f.readline().split())
        heap = []
        for i in a:
            add(heap, i)
        print(" ".join(map(str, heap)))

main()
